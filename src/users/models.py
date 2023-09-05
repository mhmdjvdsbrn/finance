from django.db import models
from django.contrib.auth.models import PermissionsMixin 
from django.contrib.auth.models import AbstractBaseUser 
from django.contrib.auth.models import BaseUserManager as BUM 
from enum import Enum



class BaseModel(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseUserManager(BUM):
    def create_user(self, email,full_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email.lower()),full_name=full_name)

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

class CustomerStatus(Enum):
    NORMAL = 'Normal'
    BRONZE = 'Bronze'
    SILVER = 'Silver'
    GOLD = 'GOLD'

class BaseUser(BaseModel ,AbstractBaseUser ,PermissionsMixin):

    GENDER_CHOICES = [
        ('N', 'Normal'),
        ('B', 'Bronze'),
        ('S', 'Silver'),
        ('G', 'Gold'),

    ]
    email = models.EmailField(verbose_name="email address", unique=True)
    full_name = models.CharField(max_length=35)
    customer_status = models.CharField(max_length=1, choices=GENDER_CHOICES, default='N')


    objects = BaseUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def is_staff(self):
        return self.is_admin

