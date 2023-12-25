from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    custom user model manager where email is the unique identifiers for authentication instead of username.
    """

    def create_user(self, first_name, last_name, email, password, **extra_fields):
        """
        Create and save a user with the given name, email and password.
        """

        if not email:
            raise ValueError(_("Email address is required."))
        if not password:
            raise ValueError(_("Password is required."))
        email = self.normalize_email(email)
        extra_fields.setdefault("is_verified", True)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.first_name = first_name.title()
        user.last_name = last_name.title()
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name, last_name, email, password, **extra_fields):
        """
        Create and save a super_user with the given name, email and password.
        """

        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(first_name, last_name, email, password, **extra_fields)
