from django_socio_grpc import generics
from .models import Question
from .serializers import QuestionProtoSerializer

from django_socio_grpc.decorators import grpc_action
from .grpc import app_example_pb2


class QuestionService(generics.AsyncModelService):
    queryset = Question.objects.all()
    serializer_class = QuestionProtoSerializer

    @grpc_action(
        request=[
            {
                "name": "question_text",
                "type": "string",
            }
        ],
        response=[
            {
                "name": "response",
                "type": "string",
            }
        ],
        request_stream=True,
        response_stream=True,
    )
    async def Stream(self, request, context):
        async for question in request:
            print("Question received :")
            print(question.question_text)
            yield app_example_pb2.QuestionStreamResponse(response=input("Give response\n"))
