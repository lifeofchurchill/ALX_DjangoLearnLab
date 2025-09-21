from django.contrib.auth.decorators import permission_required

@permission_required('relationship_app.can_create', raise_exception=True)
def add_book(request):
    # logic to add book
    pass

@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, pk):
    # logic to edit book
    pass

@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, pk):
    # logic to delete book
    pass
