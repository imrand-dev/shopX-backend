from datetime import date

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from autoslug import AutoSlugField

from phonenumber_field.modelfields import PhoneNumberField

from versatileimagefield.fields import VersatileImageField, PPOIField

from core.choices import UserStatus, EmploymentStatus, UserGender
from core.managers import CustomUserManager
from core.utils import full_name

from common.base_model import BaseModelWithUID


class User(AbstractBaseUser, PermissionsMixin, BaseModelWithUID):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    slug = AutoSlugField(
        populate_from=full_name,
        editable=False,
        unique=True,
    )
    phone = PhoneNumberField(null=True, blank=True, unique=True)
    email = models.EmailField(unique=True, db_index=True)
    avatar = VersatileImageField(
        verbose_name="Profile Picture",
        upload_to="assets/avatar",
        null=True,
        blank=True,
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=True)
    role = models.CharField(
        max_length=15,
        choices=UserStatus.choices,
        default=UserStatus.CUSTOMER,
    )
    employment = models.CharField(
        max_length=15,
        choices=EmploymentStatus.choices,
        default=EmploymentStatus.UNKNOWN,
    )
    date_of_birth = models.DateField(default=date(year=1970, month=1, day=1))
    gender = models.CharField(
        max_length=10,
        choices=UserGender.choices,
        default=UserGender.OTHER,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone"]

    # custom manager
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        ordering = ["-created_at"]