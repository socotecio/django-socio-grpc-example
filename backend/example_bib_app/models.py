from uuid import uuid4
from django.db import models


class Author(models.Model):
    author_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name_first = models.CharField(max_length=100)
    name_last = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.name_last}, {self.name_first}"


class Publisher(models.Model):
    publisher_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state_province = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField()

    def __str__(self):
        return self.name

class PublicationCategory(models.Model):
    category_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    book_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(PublicationCategory, blank=True)
    isbn = models.CharField(max_length=20, blank=True, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

class Journal(models.Model):
    journal_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(PublicationCategory, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()
    volume = models.IntegerField(blank=True, null=True)
    issue = models.IntegerField(blank=True, null=True)
    issn = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.title

