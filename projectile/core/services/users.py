from datetime import date

from django.db.models import QuerySet

from core.choices import UserStatus, EmploymentStatus, UserGender 
from core.models import User

from rest_framework.exceptions import NotFound


class UserService:
    def create_user(
        self,
        first_name: str,
        last_name: str,
        email: str,
        phone: str,
        password: str,
        avatar: str = None,
        is_active: bool = True,
        is_staff: bool = False,
        is_verified: bool = True,
        role: UserStatus.choices = UserStatus.CUSTOMER,
        employment: UserStatus.choices = EmploymentStatus.UNKNOWN,
        date_of_birth: date = date(year=1970, month=1, day=1),
        gender: UserStatus.choices = UserGender.OTHER
    ) -> User:
        return User.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
            email=email,
            avatar=avatar,
            role=role,
            is_active=is_active,
            is_staff=is_staff,
            is_verified=is_verified,
            employment=employment,
            date_of_birth=date_of_birth,
            gender=gender,
        )

    def create_superuser(
        self,
        first_name: str,
        last_name: str,
        email: str,
        phone: str,
        password: str,
        avatar: str = None,
        is_active: bool = True,
        is_staff: bool = False,
        is_verified: bool = True,
        role: UserStatus.choices = UserStatus.CUSTOMER,
        employment: UserStatus.choices = EmploymentStatus.UNKNOWN,
        date_of_birth: date = date(year=1970, month=1, day=1),
        gender: UserStatus.choices = UserGender.OTHER
    ) -> User:
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
            email=email,
            avatar=avatar,
            role=role,
            is_active=is_active,
            is_staff=is_staff,
            is_verified=is_verified,
            is_superuser = True,
            employment=employment,
            date_of_birth=date_of_birth,
            gender=gender,
        )
    
    def get_user_by_phone(self, phone: str) -> User:
        return User.objects.get(phone=phone)

    def get_user_by_email(self, email: str) -> User:
        return User.objects.get(email=email)
    
    def get_user_by_uid(self, uid: str) -> User:
        return User.objects.get(uid=uid)
