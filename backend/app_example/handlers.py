from django_socio_grpc.services.app_handler_registry import AppHandlerRegistry
from app_example.services import QuestionService


def grpc_handlers(server):
    app_registry = AppHandlerRegistry("app_example", server)
    app_registry.register(QuestionService)
