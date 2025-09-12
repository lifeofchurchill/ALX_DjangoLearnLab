from bookshelf.models import Book

# Retrieve the book we created
book = Book.objects.get(id=book.id)
print(book.title, book.author, book.publication_year)
# Expected Output: 1984 George Orwell 1949
