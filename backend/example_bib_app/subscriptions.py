import asyncio
from concurrent.futures import ThreadPoolExecutor
import queue as q
import time
from typing import Any, Dict
import uuid

import django.db.models.signals as signals

from django_socio_grpc import generics
from django_socio_grpc.decorators import grpc_action
from django_socio_grpc.grpc_actions.placeholders import SelfSerializer
from django_socio_grpc.services.app_handler_registry import AppHandlerRegistry

from django_socio_grpc import proto_serializers
from django.db import models


# goes here because its needed for the serializer only
class Subscription(models.Model):
    """
    This model is not for persistence in the database, but only to be used to create a Serializer
    """
    signal = models.TextField()


# or try to remove the model entirely
class SubscriptionProtoSerializer(proto_serializers.ModelProtoSerializer):
    """
    A serializer for the subscription request.

    Note: consider different requests per signal, like: SubscribeForUpdates, SubscribeForDeletions, etc.
    """
    class Meta:
        model = Subscription
        fields = ["signal"]


class ModelSignalDispatcher:
    """
    Dispatches Django model signals "post_init" (read), "post_save" (create/update) and "post_delete" (delete)
    to the GRPC clients that subscribed for them using Subscribe(signal="post_save").

    Django signals are handled synchronously, so we decouple that by making use of a simple queue per subscription.
    The queues are consumed by the Subscribe(), so if a client takes very long when handling the events, only that client will
    have its events accumulate, other clients will be faster.

    Furthermore, client listeners are health-monitored to be able to shutdown the handler thread should there be no more listeners
    for a given model signal. This can introduce a delay for models changing at a frequency considerably higher than the heartbeat
    interval.

    Considerations:
    - Set property interval_seconds according to the needs of your models.
    - For each signal, it runs a handler thread, so Django signal's connect() method is called at max 3 times per model,
    needed threads for your app are thus (number of subscribable models) * 3.
    - Slow running subscription clients could possibly be accumulating memory in the subscription queue. Maybe safeguard this.
    """
    
    event_listeners: Dict[str, Dict[str, Any]] = {}
    executor: ThreadPoolExecutor() = None
    interval_seconds = 0.1

    def __init__(self, app_name: str, model_name: str):
        print(f"Creating ModelSignalDispatcher for {app_name}.{model_name}Service")

        self.app_name = app_name
        self.model_name = model_name
        self.consumer_futures = {
            "post_init": None,
            "post_save": None,
            "post_delete": None,
        }
        self.event_listeners = {"post_init": {}, "post_save": {}, "post_delete": {}}
        self.executor = ThreadPoolExecutor()

    def subscribe(self, signal="post_save") -> str:
        print("subscribing for", self.model_name, signal)

        if signal not in self.event_listeners:
            raise ValueError(
                f"Cannot subscribe to signal {signal}. Supported signal are {self.event_listeners.keys()}."
            )

        subscription_id = uuid.uuid4()

        event_queue = q.Queue()
        self.event_listeners[signal][subscription_id] = (True, event_queue)
        if (
            self.consumer_futures[signal] is None
            or not self.consumer_futures[signal].running()
        ):
            print("+++ Starting dispatcher thread for:", signal)
            self.consumer_futures[signal] = self.executor.submit(
                self.get_signal_watcher(signal)
            )
        return subscription_id

    def remove_listener(self, subscription_id) -> None:
        for signal_listeners in self.event_listeners.values():
            if subscription_id in signal_listeners:
                del signal_listeners[subscription_id]

    def set_alive(self, subscription_id):
        """
        Set a certain listener to alive.
        """
        for signal_listeners in self.event_listeners.values():
            if subscription_id in signal_listeners:
                (_, events) = signal_listeners[subscription_id]
                signal_listeners[subscription_id] = (True, events)

    async def a_wait(self, subscription_id) -> None:
        """
        Send a heartbeat and wait asynchronously
        """
        self.set_alive(subscription_id)
        await asyncio.sleep(self.interval_seconds)

    def wait(self, subscription_id) -> None:
        """
        Send a heartbeat and wait synchronously
        """
        self.set_alive(subscription_id)
        time.sleep(self.interval_seconds)

    def get_signal_watcher(self, signal):
        """
        Selects the appropriate django signal and corresponding watcher
        """
        def signal_watcher() -> None:
            try:
                handler = self.get_handler(signal)
                sender = f"{self.app_name}.{self.model_name}"
                signal_module = getattr(signals, signal)

                signal_module.connect(handler, sender=sender)
                print("+++ Connected Django signal for:", sender, signal)

                while len(self.event_listeners[signal].keys()) != 0:
                    for [
                        subscription_id,
                        (alive, _),
                    ] in (
                        self.event_listeners[signal].copy().items()
                    ):
                        if not alive:
                            self.remove_listener(subscription_id)
                        else:
                            (_, events) = self.event_listeners[signal][subscription_id]
                            self.event_listeners[signal][subscription_id] = (False, events)

                    time.sleep(self.interval_seconds * 2)

                signal_module.disconnect(handler, sender=sender)
                print("!!! Disonnected Django signal for sender: ", sender, signal)
            except Exception as e:
                print("whoops!", e)

        return signal_watcher

    def get_handler(self, signal):
        if signal == "post_save":
            return self.post_save_handler
        if signal == "post_init":
            return self.post_init_handler
        if signal == "post_delete":
            return self.post_delete_handler
        raise ValueError(f"No handler for signal {signal}")

    def post_init_handler(self, sender, **kwargs):
        for _, events in self.event_listeners["post_init"].values():
            events.put(kwargs["instance"])

    def post_save_handler(self, sender, **kwargs):
        for _, events in self.event_listeners["post_save"].values():
            events.put(kwargs["instance"])

    def post_delete_handler(self, sender, **kwargs):
        for _, events in self.event_listeners["post_delete"].values():
            events.put(kwargs["instance"])

    def get_events(self, subscription_id) -> q.Queue:
        for signal_listeners in self.event_listeners.values():
            if subscription_id in signal_listeners:
                (_, events) = signal_listeners[subscription_id]
                return events

        # return an empty queue
        return q.Queue()


class ModelSignalDispatcherStore:
    """
    A factory and storage for a per-model singleton instance of
    ModelSignalDispatcher.

    This store has to live some place singular per app.
    """
    _signal_dispatchers: Dict[str, ModelSignalDispatcher] = {}
    _app_name: None

    def __init__(self, app_name):
        self.app_name = app_name

    def get_dispatcher_for_model(self, model: str) -> ModelSignalDispatcher:
        if model not in self._signal_dispatchers:
            self._signal_dispatchers[model] = ModelSignalDispatcher(
                self.app_name, model
            )
        return self._signal_dispatchers[model]


class AppHandlerRegistryWithModelSignalDispatchers(AppHandlerRegistry):
    """
    Adds a dispatcher for django signals to every registered service
    """

    _signal_dispatcher_store: ModelSignalDispatcherStore = None

    def __init__(self, app_name, server):
        self._signal_dispatcher_store = ModelSignalDispatcherStore(app_name)
        super().__init__(app_name, server)

    def get_event_dispatcher(self, model: str) -> ModelSignalDispatcher:
        return self._signal_dispatcher_store.get_dispatcher_for_model(model)


class EventDispatcherMixin(generics.GenericService):
    """
    Mix an EventDispatcher into a GenericService
    """

    @property
    def event_dispatcher(self) -> ModelSignalDispatcher:
        # maybe there's a more socio-django way of storing/retrieving the
        # event dispatcher for a given model
        # Note: get_service_name() == model, so e.g. "Question"
        return self._app_handler.get_event_dispatcher(self.get_service_name())


class SubscribeMixin(EventDispatcherMixin):
    """
    Mixin for creating a service that provides a ``Subscribe()``
    handler.
    """

    @grpc_action(
        request=SubscriptionProtoSerializer,
        response=SelfSerializer,
        response_stream=True,
    )
    def Subscribe(self, request, context):
        try:
            subscription_id = self.event_dispatcher.subscribe(request.signal)

            # here we can determine if the context is active
            while context.is_active():
                # consume events one by one, yield, wait for next
                events = self.event_dispatcher.get_events(subscription_id)
                while not events.empty():
                    serializer = self.get_serializer(events.get())
                    # syncronous API needs to yield message
                    yield serializer.message

                self.event_dispatcher.wait(subscription_id)

        except Exception as e:
            print("GRPC Subscribe failed:", e)
            raise e


class AsyncSubscribeMixin(EventDispatcherMixin):
    """
    Mixin for creating an asnyc model service that provides a ``Subscribe()``
    handler.
    """

    @grpc_action(
        request=SubscriptionProtoSerializer,
        response=SelfSerializer,
        response_stream=True,
    )
    async def Subscribe(self, request, context):
        try:
            subscription_id = self.event_dispatcher.subscribe(request.signal)

            # TODO the coroutine is cancelled when the client hangs up, so we
            # introduce a heartbeat mechanism at the event_dispatcher
            while True:
                # consume events one by one, yield, wait for next
                events = self.event_dispatcher.get_events(subscription_id)
                while not events.empty():
                    serializer = await self.aget_serializer(events.get())

                    # async context has a write function
                    await context.write(await serializer.amessage)

                await self.event_dispatcher.a_wait(subscription_id)

        except Exception as e:
            print("GRPC Subscribe failed:", e)
            raise e


class ModelServiceWithSubscribe(SubscribeMixin, generics.ModelService):
    """
    Adds ``Subscribe()`` handler to a ModelService
    """


class AsyncModelServiceWithSubscribe(
    AsyncSubscribeMixin, generics.AsyncModelService
):
    """
    Adds ``Subscribe()`` handler to a AsyncModelService
    """
