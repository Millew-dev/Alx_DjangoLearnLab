from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author_name}:")
for book in books_by_author:
    print(book.title)

# 2. List all books in a library
library_name = "Main Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"\nBooks in {library_name}:")
for book in books_in_library:
    print(book.title)

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"\nLibrarian for {library_name}: {librarian.name}")
