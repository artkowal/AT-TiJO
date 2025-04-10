from lab07_atrapy.src.library_repository  import LibraryRepository

class Library:
    def __init__(self, repository: LibraryRepository):
        self.repository = repository

    def borrow_book(self, title: str) -> bool:
        return self.repository.remove_book(title)

    def return_book(self, title: str, author: str, year: int):
        self.repository.add_book(title, author, year)

    def list_books(self):
        return self.repository.get_all_books()

if __name__ == '__main__':
    from lab07_atrapy.src.library_repository import InMemoryRepository

    repo = InMemoryRepository()
    library = Library(repo)

    library.return_book("Czysty kod", "Robert C. Martin", 2008)
    library.return_book("Python 101", "Michael Driscoll", 2019)

    print("Książki w bibliotece:", library.list_books())

    if library.borrow_book("Czysty kod"):
        print("Książka 'Czysty kod' została wypożyczona.")
    else:
        print("Książka 'Czysty kod' nie jest dostępna.")

    print("Książki w bibliotece po wypożyczeniu", library.list_books())

