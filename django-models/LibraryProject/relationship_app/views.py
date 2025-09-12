from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Book

def list_books(request):
    # Fetch all books
    books = Book.objects.all()
    
    # Pass them to the template
    context = {'book_list': books}
    
    return render(request, "relationship_app/list_books.html", context)
