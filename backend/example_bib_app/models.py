from uuid import uuid4
from django.db import models
from django.utils import timezone


class Author(models.Model):
    """ Author of a publication"""
    author_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name_first = models.CharField(max_length=100, help_text="First name of the author")
    name_last = models.CharField(max_length=100, help_text="Last name of the author")
    birth_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name_last}, {self.name_first}"


class Publisher(models.Model):
    """ Publisher of a publication"""
    publisher_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100, help_text="Name of the publisher")
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state_province = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField()

    def __str__(self):
        return self.name

class PublicationCategory(models.Model):
    """ Category of a publication, like 'book', 'journal', 'magazine', 'scientific article', etc.
    """
    category_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """ Book model"""
    book_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(PublicationCategory, blank=True)
    isbn = models.CharField(max_length=20, blank=True, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

class Journal(models.Model):
    """ Journal model"""
    journal_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(PublicationCategory, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField(default=timezone.now)
    volume = models.IntegerField(blank=True, null=True)
    issue = models.IntegerField(blank=True, null=True)
    issn = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.title

