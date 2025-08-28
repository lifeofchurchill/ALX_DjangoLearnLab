from django.contrib import admin
from .models import Book

# Register your models here.
# Register Book model with the default admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')   # show these fields in the list view
    search_fields = ('title', 'author')                      # add search box for title and author
    list_filter = ('publication_year',)                      # add filter by publication year
