"""
GitHub Copilot: The selected code is a Python module named `admin.py`. This module defines the Django admin interface configuration for several models: `Author`, `Publisher`, `PublicationCategory`, `Book`, and `Journal`.
 The module imports the `admin` module from the `django.contrib` package, which provides the base classes for the admin interface.

Each model is registered with the admin interface using the `@admin.register` decorator. The decorator takes the model class as an argument and 
returns a class that extends the `ModelAdmin` class from the `admin` module. The extended class defines the display fields for the model in the admin interface using the 
`list_display` attribute. The `list_display` attribute is a tuple of field names that are displayed in the list view of the model in the admin interface.

The `PublisherAdmin` class defines a docstring that describes the purpose of the class. The docstring is used to generate documentation for the class and should provide a clear and concise explanation of the class's functionality.

Overall, this module provides a convenient way to configure the Django admin interface for the specified models. To improve the readability of the code, the docstrings for 
the other admin classes could be added as well. Additionally, the `list_display` attributes could be grouped by their type (e.g., name fields, date fields) to make it easier to see which fields are being displayed.

(Copilot 20231015 )
"""
from django.contrib import admin

# Register your models here.

from .models import Author, Publisher, PublicationCategory, Book, Journal


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name_first', 'name_last', 'birth_date')

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Publisher model.

    The PublisherAdmin class defines the display fields for the Publisher model
    in the Django admin interface.
    """
    list_display = ('name', 'address', 'city', 'state_province', 'country', 'website')

@admin.register(PublicationCategory)
class PublicationCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'publisher', 'publication_date')

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_datetime', 'volume', 'issue', 'issn')

