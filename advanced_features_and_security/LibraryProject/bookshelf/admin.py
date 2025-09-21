from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Book


# Register your models here.
# Register Book model with the default admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')   # show these fields in the list view
    search_fields = ('title', 'author')                      # add search box for title and author
    list_filter = ('publication_year',)                      # add filter by publication year



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )


# Create groups
editors, created = Group.objects.get_or_create(name="Editors")
viewers, created = Group.objects.get_or_create(name="Viewers")
admins, created = Group.objects.get_or_create(name="Admins")

# Get permissions
content_type = ContentType.objects.get_for_model(Book)
can_edit = Permission.objects.get(codename="can_edit", content_type=content_type)
can_create = Permission.objects.get(codename="can_create", content_type=content_type)
can_view = Permission.objects.get(codename="can_view", content_type=content_type)
can_delete = Permission.objects.get(codename="can_delete", content_type=content_type)

# Assign permissions to groups
editors.permissions.set([can_edit, can_create])
viewers.permissions.set([can_view])
admins.permissions.set([can_view, can_create, can_edit, can_delete])


admin.site.register(CustomUser, CustomUserAdmin)
