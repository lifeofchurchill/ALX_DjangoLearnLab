from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    """
    ExampleForm for adding or editing a Book.
    Ensures data validation and secure input handling.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn']  # adjust fields as per your Book model
