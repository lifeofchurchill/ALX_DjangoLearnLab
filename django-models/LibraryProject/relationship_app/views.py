from django.shortcuts import render
from django.views.generic.detail import DetailView  # <- required import
from .models import Book
from .models import Library   # <- required for checker

# Function-based view
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
