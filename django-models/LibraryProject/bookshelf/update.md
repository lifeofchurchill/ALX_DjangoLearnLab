from bookshelf.models import Book

# Update the title of the book
book = Book.objects.get(id=book.id)
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
