from uuid import uuid4
from django.db import models


class Author(models.Model):
    author_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name_first = models.CharField(max_length=100)
    name_last = models.CharField(max_length=100)
    birth_date = models.DateField()


class Publisher(models.Model):
    publisher_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    website = models.URLField()

class PublicationCategory(models.Model):
    category_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)

class Book(models.Model):
    book_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(PublicationCategory)
    isbn = models.CharField(max_length=20)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()

class Journal(models.Model):
    journal_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(PublicationCategory)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()
    volume = models.IntegerField()
    issue = models.IntegerField()
    issn = models.CharField(max_length=20)

