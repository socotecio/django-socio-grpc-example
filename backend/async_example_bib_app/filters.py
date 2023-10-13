import django_filters
from django_filters.rest_framework import UUIDFilter

from .models import Author, Publisher, PublicationCategory, Book, Journal


class AuthorFilterSet(django_filters.FilterSet):
    #id = UUIDFilter(field_name='id')

    class Meta:
        model = Author
        fields = ['name_first', 'name_last']  #  { 'name_first': ['contains'], 'name_last':['contains']}