from django_socio_grpc import proto_serializers
from rest_framework.serializers import UUIDField, PrimaryKeyRelatedField

from .models import Author, Publisher, PublicationCategory, Book, Journal

from sync_example_bib_app.grpc.sync_example_bib_app_pb2 import (
    AuthorResponse, AuthorListResponse,
    PublisherResponse, PublisherListResponse,
    PublicationCategoryResponse, PublicationCategoryListResponse,
    BookResponse, BookListResponse,
    JournalResponse, JournalListResponse
)

class AuthorProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Author
        fields = ["author_id", "name_first", "name_last", "birth_date"]

        proto_class = AuthorResponse
        proto_class_list = AuthorListResponse

class PublisherProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Publisher
        fields = ["publisher_id", "name", "address", "city", "state_province", "country", "website"]

        proto_class = PublisherResponse
        proto_class_list = PublisherListResponse

class PublicationCategoryProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = PublicationCategory
        fields = ["category_id", "name"]

        proto_class = PublicationCategoryResponse
        proto_class_list = PublicationCategoryListResponse

class BookProtoSerializer(proto_serializers.ModelProtoSerializer):
    categories = PrimaryKeyRelatedField(queryset=PublicationCategory.objects.all(), pk_field=UUIDField(format="hex_verbose"), many=True)
    authors = PrimaryKeyRelatedField(queryset=Author.objects.all(), pk_field=UUIDField(format="hex_verbose"), many=True)

    publisher = PrimaryKeyRelatedField(queryset=Publisher.objects.all(), pk_field=UUIDField(format="hex_verbose"))

    class Meta:
        model = Book
        fields = ["book_id", "title", "authors", "categories", "isbn", "publisher", "publication_date"]

        proto_class = BookResponse
        proto_class_list = BookListResponse

class JournalProtoSerializer(proto_serializers.ModelProtoSerializer):

    categories = PrimaryKeyRelatedField(queryset=PublicationCategory.objects.all(), pk_field=UUIDField(format="hex_verbose"), many=True)
    authors = PrimaryKeyRelatedField(queryset=Author.objects.all(), pk_field=UUIDField(format="hex_verbose"), many=True)
    
    publisher = PrimaryKeyRelatedField(queryset=Publisher.objects.all(), pk_field=UUIDField(format="hex_verbose"))

    class Meta:
        model = Journal
        fields = ["journal_id", "title", "authors", "categories", "publisher", "publication_date", "volume", "issue", "issn"]

        proto_class = JournalResponse
        proto_class_list = JournalListResponse
        

