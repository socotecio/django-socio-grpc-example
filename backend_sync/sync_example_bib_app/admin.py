from django.contrib import admin

# Register your models here.

from .models import Author, Publisher, PublicationCategory, Book, Journal


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name_first', 'name_last', 'birth_date')

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state_province', 'country', 'website')

@admin.register(PublicationCategory)
class PublicationCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'publisher', 'publication_date')

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date', 'volume', 'issue', 'issn')

