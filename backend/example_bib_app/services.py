
"""
GitHub Copilot: The selected code is a Python module named `services.py`. This module defines several gRPC service classes for the `example_bib_app` application. 
The module imports several modules from the same application, including `models`, `serializers`, and `filters`. 
The module also imports the `generics` module from the `django_socio_grpc` package, which provides base classes for gRPC services.

The module defines five service classes: `AuthorService`, `PublisherService`, `PublicationCategoryService`, `BookService`, and `BookStreamingService`. 
Each service class extends the `AsyncModelService` class from the `generics` module and defines a `queryset` attribute that specifies the Django model to be used,
 a `filterset_class` attribute that specifies the filter class to be used (if any), and a `serializer_class` attribute that specifies the serializer class to be used.

The `AuthorService` class defines `filterset_fields` instead of `filterset_class`. This attribute allows for filtering of the queryset based on exact matches.
 For more complex filtering, the `filterset_class` attribute can be used instead.

The `PublisherService` class defines `filterset_class` instead of `filterset_fields`. This attribute allows for filtering of the queryset using a custom filter class named `PublisherFilterSet`.

The `BookService` class also defines `filterset_class` using a custom filter class named `BookFilterSet`. Additionally, the `BookStreamingService` class is defined to stream books to the client. 
The `Stream` method is decorated with the `@grpc_action` decorator, which specifies the request and response message types, as well as the request and response stream types.

Overall, this module provides a convenient way to define gRPC services for the specified models in the `example_bib_app` application. To improve the readability of the code, 
the `filterset_fields` and `filterset_class` attributes could be grouped by their type (e.g., author-related filters, publisher-related filters) to make it easier to see which filters are being used. 
Additionally, the `BookStreamingService` class could be moved to a separate module to improve the organization of the code.
"""
from django_socio_grpc import generics
from django_socio_grpc.decorators import grpc_action

from .models import Author, Publisher, PublicationCategory, Book, Journal

from .serializers import AuthorProtoSerializer, PublisherProtoSerializer, PublicationCategoryProtoSerializer, BookProtoSerializer, JournalProtoSerializer

from .filters import PublisherFilterSet, BookFilterSet

class AuthorService(generics.AsyncModelService):
    queryset = Author.objects.all()

    # filterset_fields allows for filtering of the queryset, only based on exact matches.
    # for more complex filtering, use filterset_class
    filterset_fields = ('name_first', 'name_last',)
    serializer_class = AuthorProtoSerializer

class PublisherService(generics.AsyncModelService):
    queryset = Publisher.objects.all()

    # the optional filterset_class allows for filtering of the queryset (s. filter client example)
    filterset_class = PublisherFilterSet
    serializer_class = PublisherProtoSerializer

class PublicationCategoryService(generics.AsyncModelService):
    queryset = PublicationCategory.objects.all()
    serializer_class = PublicationCategoryProtoSerializer

class BookService(generics.AsyncModelService):
    queryset = Book.objects.all()
    filterset_class = BookFilterSet
    serializer_class = BookProtoSerializer

# Book Streaming Service
# This service is used to stream books to the client.
# The client can request a stream of books by sending a request with a list of book ids.

class BookStreamingService(generics.AsyncModelService):
    queryset = Book.objects.all()
    serializer_class = BookProtoSerializer

    @grpc_action(
        request=[
            {
                "name": "book_ids",
                "type": "string",
            }
        ],
        response=[
            {
                "name": "book",
                "type": "BookResponse",
            }
        ],
        request_stream=True,
        response_stream=True,
    )
    async def Stream(self, request, context):
        for book_id in request.book_ids:
            book = await self.get_object(book_id)
            yield book


class JournalService(generics.AsyncModelService):
    queryset = Journal.objects.all()
    serializer_class = JournalProtoSerializer

    # filterset_fields allows for filtering of the queryset,
    # mind that it is also possible to filter on related fields with '__' (e.g. publisher__name)
    search_fields = ("title", "authors__name_first", "authors__name_last", "publisher__name", "categories__name", "issn",)


#from .models import Question
#from .serializers import QuestionProtoSerializer

# class QuestionService(generics.AsyncModelService):
#     queryset = Question.objects.all()
#     serializer_class = QuestionProtoSerializer

#     @grpc_action(
#         request=[
#             {
#                 "name": "question_text",
#                 "type": "string",
#             }
#         ],
#         response=[
#             {
#                 "name": "response",
#                 "type": "string",
#             }
#         ],
#         request_stream=True,
#         response_stream=True,
#     )
#     async def Stream(self, request, context):
#         async for question in request:
#             print("Question received :")
#             print(question.question_text)
#             yield example_bib_app_pb2.QuestionStreamResponse(response=input("Give response\n"))
