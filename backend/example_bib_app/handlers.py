"""
GitHub Copilot: The selected code is a Python module named `handlers.py`. This module defines a function named `grpc_handlers` that registers gRPC service handlers for several services provided by
 the `example_bib_app` application. The module imports the `AppHandlerRegistry` class from the `django_socio_grpc.services.app_handler_registry` module and the service classes from the `example_bib_app.services` module.

The `grpc_handlers` function takes a `server` argument, which is an instance of the `grpc.aio.Server` class from the `grpc` module. The function creates an instance of the `AppHandlerRegistry` class,
 passing the name of the application and the `server` instance as arguments. The `AppHandlerRegistry` class is a utility class that simplifies the registration of gRPC service handlers in Django applications.

The function then registers the service classes with the `AppHandlerRegistry` instance using the `register` method. The `register` method takes a service class as an argument and creates a gRPC service handler for the class. 
The service classes that are registered are `AuthorService`, `PublisherService`, `PublicationCategoryService`, `BookService`, and `JournalService`.

The `# QuestionService` line is commented out, which means that the `QuestionService` class is not registered with the `AppHandlerRegistry` instance. This line could be uncommented if the `QuestionService` class is implemented 
and needs to be registered as a gRPC service handler.

Overall, this module provides a convenient way to register gRPC service handlers for the specified services in the `example_bib_app` application. 
To improve the readability of the code, the `register` method calls could be grouped by service type (e.g., author-related services, publisher-related services) to make 
it easier to see which services are being registered. Additionally, the commented-out `QuestionService` registration could be removed if the class is not needed.
"""

from django_socio_grpc.services.app_handler_registry import AppHandlerRegistry
from example_bib_app.services import (
    AuthorService,
    PublisherService,
    PublicationCategoryService,
    BookService,
    JournalService,
)


def grpc_handlers(server):
    app_registry = AppHandlerRegistry("example_bib_app", server)
    app_registry.register(AuthorService)
    app_registry.register(PublisherService)
    app_registry.register(PublicationCategoryService)
    app_registry.register(BookService)
    app_registry.register(JournalService)

    # QuestionService
    # app_registry.register(QuestionService)
