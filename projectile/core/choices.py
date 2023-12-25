from django.db import models


class UserStatus(models.TextChoices):
    SUPER_USER = "SUPER_USER", "Super User"
    STAFF = "STAFF", "Staff"
    CUSTOMER = "CUSTOMER", "Customer"


class EmploymentStatus(models.TextChoices):
    FULL_TIME = "FULL_TIME", "Full Time"
    PART_TIME = "PART_TIME", "Part Time"
    TRAINEE = "TRAINEE", "Trainee"
    UNKNOWN = "UNKNOWN", "Unknown"


class UserGender(models.TextChoices):
    MALE = "MALE", "Male"
    EFMALE = "FEMALE", "Female"
    OTHER = "OTHER", "Other"