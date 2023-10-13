from django_filters.rest_framework import FilterSet, CharFilter

from .models import Author


class AuthorFilterSet(FilterSet):

    name_last = CharFilter(field_name="name_last", lookup_expr="contains")

    class Meta:
        model = Author
        fields = ['name_first', 'name_last']  #  { 'name_first': ['contains'], 'name_last':['contains']}