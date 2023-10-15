from django.test import TestCase

# Create your tests here.
from .serializers import BookSerializer
from .services import BookService

class BookSerializerTestCase(TestCase):
    def test_book_serializer(self):
        book_data = {
            'title': 'The Great Gatsby',
            'author': 'F. Scott Fitzgerald',
            'published_date': '1925-04-10',
            'isbn': '978-3-16-148410-0',
        }
        serializer = BookSerializer(data=book_data)
        self.assertTrue(serializer.is_valid())
        book = serializer.save()
        self.assertEqual(book.title, 'The Great Gatsby')
        self.assertEqual(book.author, 'F. Scott Fitzgerald')
        self.assertEqual(book.published_date, '1925-04-10')
        self.assertEqual(book.isbn, '978-3-16-148410-0')

class BookServiceTestCase(TestCase):
    def test_book_service(self):
        book_data = {
            'title': 'The Great Gatsby',
            'author': 'F. Scott Fitzgerald',
            'published_date': '1925-04-10',
            'isbn': '978-3-16-148410-0',
        }
        book = BookService.create_book(book_data)
        self.assertEqual(book.title, 'The Great Gatsby')
        self.assertEqual(book.author, 'F. Scott Fitzgerald')
        self.assertEqual(book.published_date, '1925-04-10')
        self.assertEqual(book.isbn, '978-3-16-148410-0')
        book.title = 'The Catcher in the Rye'
        updated_book = BookService.update_book(book.id, book)
        self.assertEqual(updated_book.title, 'The Catcher in the Rye')
        BookService.delete_book(book.id)
        with self.assertRaises(Book.DoesNotExist):
            BookService.get_book(book.id)