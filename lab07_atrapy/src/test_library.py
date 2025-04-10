import unittest
from unittest.mock import Mock
from lab07_atrapy.src.library import Library
from lab07_atrapy.src.library_repository import LibraryRepository

class LibraryTestCase(unittest.TestCase):

    def test_borrow_book_calls_remove_book(self):
        mock_repo = Mock(spec=LibraryRepository)
        mock_repo.remove_book.return_value = True

        library = Library(mock_repo)
        result = library.borrow_book("Akademia Pana Kleksa")

        self.assertTrue(result)
        mock_repo.remove_book.assert_called_once_with("Akademia Pana Kleksa")

    def test_return_book_calls_add_book(self):
        mock_repo = Mock(spec=LibraryRepository)
        library = Library(mock_repo)

        library.return_book("Book Title", "Author", 2025)
        mock_repo.add_book.assert_called_once_with("Book Title", "Author", 2025)

    def test_list_books_calls_get_all_books(self):
        mock_repo = Mock(spec=LibraryRepository)
        expected_books = [("Book Title", "Author", 2025)]
        mock_repo.get_all_books.return_value = expected_books

        library = Library(mock_repo)
        books = library.list_books()

        self.assertEqual(books, expected_books)
        mock_repo.get_all_books.assert_called_once()

if __name__ == '__main__':
    unittest.main()