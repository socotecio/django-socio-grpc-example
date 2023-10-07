from django_socio_grpc import generics
from django_socio_grpc.decorators import grpc_action

from .models import Author, Publisher, PublicationCategory, Book, Journal

from .serializers import AuthorProtoSerializer, PublisherProtoSerializer, PublicationCategoryProtoSerializer, BookProtoSerializer, JournalProtoSerializer


class AuthorService(generics.ModelService):
    queryset = Author.objects.all()
    serializer_class = AuthorProtoSerializer

class PublisherService(generics.ModelService):
    queryset = Publisher.objects.all()
    serializer_class = PublisherProtoSerializer

class PublicationCategoryService(generics.ModelService):
    queryset = PublicationCategory.objects.all()
    serializer_class = PublicationCategoryProtoSerializer

class BookService(generics.ModelService):
    queryset = Book.objects.all()
    serializer_class = BookProtoSerializer

class JournalService(generics.ModelService):
    queryset = Journal.objects.all()
    serializer_class = JournalProtoSerializer



#from .models import Question
#from .serializers import QuestionProtoSerializer

# class QuestionService(generics.ModelService):
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
#      def Stream(self, request, context):
#          for question in request:
#             print("Question received :")
#             print(question.question_text)
#             yield _example_bib_app_pb2.QuestionStreamResponse(response=input("Give response\n"))
