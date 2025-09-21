# CRUD Operations with the Book Model

This document shows Create, Retrieve, Update, and Delete operations for the `Book` model using the Django shell.

---

## Create
```python
from bookshelf.models import Book

# Create a book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
# Expected Output: 1984 by George Orwell (1949)

RETRIEVE
from bookshelf.models import Book

# Retrieve the book we created
book = Book.objects.get(id=book.id)
print(book.title, book.author, book.publication_year)
# Expected Output: 1984 George Orwell 1949

# Or retrieve all books
Book.objects.all()
# Expected Output: <QuerySet [<Book: 1984 by George Orwell (1949)>]>

UPDATE
from bookshelf.models import Book

# Update the title of the book
book = Book.objects.get(id=book.id)
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
# Expected Output: Nineteen Eighty-Four

DELETE
from bookshelf.models import Book

# Delete the book
book = Book.objects.get(id=book.id)
book.delete()
# Expected Output: (1, {'bookshelf.Book': 1})
