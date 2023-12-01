from django_filters.rest_framework import FilterSet, CharFilter, DateRangeFilter

from .models import Author, Publisher, Book, Journal


class AuthorFilterSet(FilterSet):
    name_first = CharFilter(field_name="name_first", lookup_expr="contains")
    name_last = CharFilter(field_name="name_last", lookup_expr="contains")
    birth_date = DateRangeFilter(field_name="birth_date")

    class Meta:
        model = Author
        fields = fields = {
            "name_first": ["exact", "contains"],
            "name_last": ["exact", "contains"],
            "birth_date": ["exact", "contains"],
        }


class PublisherFilterSet(FilterSet):
    name = CharFilter(field_name="name", lookup_expr="contains")
    address = CharFilter(field_name="address", lookup_expr="contains")
    city = CharFilter(field_name="city", lookup_expr="contains")

    class Meta:
        model = Publisher
        fields = [
            "name",
            "address",
            "city",
        ]


class BookFilterSet(FilterSet):
    # title = CharFilter(field_name="title", lookup_expr="contains")
    # isbn = CharFilter(field_name="isbn", lookup_expr="contains")
    # publication_date = DateRangeFilter(field_name="publication_date")
    # publisher_name = CharFilter(field_name="publisher__name", lookup_expr="contains")

    class Meta:
        model = Book
        fields = {
            "title": ["exact", "contains"],
            "isbn": ["exact", "contains"],
            # "description": ["exact", "contains"],
            #'datetime_created': ['lt', 'gt'],
        }
