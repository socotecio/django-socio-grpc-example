"""
This module defines several classes that are used to serialize Django models into Protocol Buffer messages. 
Protocol Buffers are a language-agnostic data serialization format developed by Google. The module imports the `proto_serializers` module from the `django_socio_grpc` package, 
which provides the base classes for the serializers.

The module defines four serializer classes: `AuthorProtoSerializer`, `PublisherProtoSerializer`, `PublicationCategoryProtoSerializer`, `BookProtoSerializer`, and `JournalProtoSerializer`.
 Each serializer class extends the `ModelProtoSerializer` class from the `proto_serializers` module and defines a `Meta` class that specifies the Django model to be serialized, the fields
   to be included in the serialized message, and the corresponding Protocol Buffer message classes.

The `BookProtoSerializer` and `JournalProtoSerializer` classes define additional fields that are not present in the Django models. These fields are used to serialize many-to-many relationships
 between the models and are implemented using the `PrimaryKeyRelatedField` class from the `rest_framework.serializers` module. The `PrimaryKeyRelatedField` class is used to serialize a many-to-many relationship 
 as a list of primary keys, which are represented as UUIDs in this case.

Overall, this module provides a convenient way to serialize Django models into Protocol Buffer messages, which can be used to exchange data between different systems. To improve the readability of the code, 
the `Meta` classes could be moved to the top of each serializer class, and the fields could be grouped by their type (e.g., primary keys, foreign keys, many-to-many fields). 
Additionally, the `Meta` classes could be made more concise by using the `fields` attribute to specify all the fields at once instead of listing them one by one.

(Copilot 20231015 )
"""

from django_socio_grpc import proto_serializers
from rest_framework.serializers import UUIDField, PrimaryKeyRelatedField

from .models import Author, Publisher, PublicationCategory, Book, Journal

from example_bib_app.grpc.example_bib_app_pb2 import (
    AuthorResponse,
    AuthorListResponse,
    PublisherResponse,
    PublisherListResponse,
    PublicationCategoryResponse,
    PublicationCategoryListResponse,
    BookResponse,
    BookListResponse,
    JournalResponse,
    JournalListResponse,
)


class AuthorProtoSerializer(proto_serializers.ModelProtoSerializer):
    """
    A serializer class that converts Author model instances to AuthorResponse
    protocol buffer messages and vice versa.

    Attributes:
        model: The Author model class.
        fields: A list of field names to include in the serialized output.
        proto_class: The protocol buffer message class for a single Author instance.
        proto_class_list: The protocol buffer message class for a list of Author instances.
    """
    class Meta:
        model = Author
        fields = ["author_id", "name_first", "name_last", "birth_date"]

        proto_class = AuthorResponse
        proto_class_list = AuthorListResponse


class PublisherProtoSerializer(proto_serializers.ModelProtoSerializer):
    """
    A protocol buffer serializer for the Publisher model.

    This serializer defines the mapping between the Publisher model and its corresponding
    protocol buffer messages, PublisherResponse and PublisherListResponse.

    Attributes:
        Meta: A class that contains metadata about the serializer, such as the model it
            serializes, the fields to include, and the protocol buffer messages to use.
    """
    class Meta:
        model = Publisher
        fields = [
            "publisher_id",
            "name",
            "address",
            "city",
            "state_province",
            "country",
            "website",
        ]

        proto_class = PublisherResponse
        proto_class_list = PublisherListResponse


class PublicationCategoryProtoSerializer(proto_serializers.ModelProtoSerializer):
    """
    Serializer for the PublicationCategory model that converts it to a Protocol Buffer message.
    """
    class Meta:
        model = PublicationCategory
        fields = ["category_id", "name"]

        proto_class = PublicationCategoryResponse
        proto_class_list = PublicationCategoryListResponse


class BookProtoSerializer(proto_serializers.ModelProtoSerializer):
    """
    Serializer for the Book model that converts the model instance to a protobuf message.
    This serializer defines the fields that should be included in the protobuf message and how they should be serialized.
    """

    # serialisation of a many-to-many field with a UUIDField as the primary key
    categories = PrimaryKeyRelatedField(
        queryset=PublicationCategory.objects.all(),
        pk_field=UUIDField(format="hex_verbose"),
        many=True,
    )
    authors = PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        pk_field=UUIDField(format="hex_verbose"),
        many=True,
    )

    publisher = PrimaryKeyRelatedField(
        queryset=Publisher.objects.all(), pk_field=UUIDField(format="hex_verbose")
    )

    class Meta:
        model = Book
        fields = [
            "book_id",
            "title",
            "authors",
            "categories",
            "isbn",
            "publisher",
            "publication_date",
        ]

        proto_class = BookResponse
        proto_class_list = BookListResponse


class JournalProtoSerializer(proto_serializers.ModelProtoSerializer):
    """
    Serializer for the Journal model that converts the model instance to a Protocol Buffer message.
    """
    categories = PrimaryKeyRelatedField(
        queryset=PublicationCategory.objects.all(),
        pk_field=UUIDField(format="hex_verbose"),
        many=True,
    )
    authors = PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        pk_field=UUIDField(format="hex_verbose"),
        many=True,
    )

    publisher = PrimaryKeyRelatedField(
        queryset=Publisher.objects.all(), pk_field=UUIDField(format="hex_verbose")
    )

    class Meta:
        model = Journal
        fields = [
            "journal_id",
            "title",
            "authors",
            "categories",
            "publisher",
            "publication_date",
            "volume",
            "issue",
            "issn",
        ]

        proto_class = JournalResponse
        proto_class_list = JournalListResponse
