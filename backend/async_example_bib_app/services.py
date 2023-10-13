from django_socio_grpc import generics
from django_socio_grpc.decorators import grpc_action

from .models import Author, Publisher, PublicationCategory, Book, Journal

from .serializers import AuthorProtoSerializer, PublisherProtoSerializer, PublicationCategoryProtoSerializer, BookProtoSerializer, JournalProtoSerializer

from .filters import AuthorFilterSet

class AuthorService(generics.AsyncModelService):
    queryset = Author.objects.all()
    filterset_class = AuthorFilterSet
    serializer_class = AuthorProtoSerializer

class PublisherService(generics.AsyncModelService):
    queryset = Publisher.objects.all()
    serializer_class = PublisherProtoSerializer

class PublicationCategoryService(generics.AsyncModelService):
    queryset = PublicationCategory.objects.all()
    serializer_class = PublicationCategoryProtoSerializer

class BookService(generics.AsyncModelService):
    queryset = Book.objects.all()
    serializer_class = BookProtoSerializer

class JournalService(generics.AsyncModelService):
    queryset = Journal.objects.all()
    serializer_class = JournalProtoSerializer



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
#             yield async_example_bib_app_pb2.QuestionStreamResponse(response=input("Give response\n"))
