from django_socio_grpc import proto_serializers
from .models import Question
from .grpc import app_example_pb2


class QuestionProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Question
        fields = ["id", "question_text", "pub_date"]
        proto_class = app_example_pb2.QuestionResponse
        proto_class_list = app_example_pb2.QuestionListResponse
