from django_socio_grpc.services.app_handler_registry import AppHandlerRegistry
from async_example_bib_app.services import AuthorService, PublisherService, PublicationCategoryService, BookService, JournalService

def grpc_handlers(server):
    app_registry = AppHandlerRegistry("async_example_bib_app", server)
    app_registry.register(AuthorService)
    app_registry.register(PublisherService)
    app_registry.register(PublicationCategoryService)
    app_registry.register(BookService)
    app_registry.register(JournalService)

    # QuestionService
    #app_registry.register(QuestionService)
