from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings

class UserManager(BaseUserManager):        #사용자 모델 생성
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)

class User(AbstractUser):             #사용자 모델 생성
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
    




# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         # user 생성 로직
#         pass      

#     def create_superuser(self, email, password=None, **extra_fields):
#         # superuser 생성 로직
#         pass

# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     # 기타 사용자 필드들

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.email