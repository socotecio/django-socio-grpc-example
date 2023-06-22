from django_socio_grpc import generics
from .models import Question
from .serializers import QuestionProtoSerializer


class QuestionService(generics.AsyncModelService):
    queryset = Question.objects.all()
    serializer_class = QuestionProtoSerializer
