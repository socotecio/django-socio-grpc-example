from django_filters.rest_framework import FilterSet, CharFilter, DateRangeFilter

from .models import Publisher

class PublisherFilterSet(FilterSet):
    name = CharFilter(field_name="name", lookup_expr="contains")
    address = CharFilter(field_name="address", lookup_expr="contains")
    city = CharFilter(field_name="city", lookup_expr="contains")

    class Meta:
        model = Publisher
        fields = ['name', 'address', 'city',]

# book
class BookFilterSet(FilterSet):
    title = CharFilter(field_name="title", lookup_expr="contains")
    isbn = CharFilter(field_name="isbn", lookup_expr="contains")
    publication_date = DateRangeFilter(field_name="publication_date")
    publisher_name = CharFilter(field_name="publisher__name", lookup_expr="contains")

    class Meta:
        model = Publisher
        fields = ['title', 'isbn', 'publication_date', 'publisher_name',]