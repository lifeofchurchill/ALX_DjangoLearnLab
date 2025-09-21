from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    """Custom manager for CustomUser with email instead of username"""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_("The Email field must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)  # create a User object
        user.set_password(password)  # hash the password
        user.save(using=self._db)   # save to DB
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None  # remove username, we’ll use email instead
    email = models.EmailField(unique=True)

    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profiles/', null=True, blank=True)

    USERNAME_FIELD = "email"  # login with email
    REQUIRED_FIELDS = ["date_of_birth"]  # extra fields when creating superuser

    objects = CustomUserManager()  # attach manager

    def __str__(self):
        return self.email
