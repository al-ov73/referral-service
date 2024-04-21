from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.crypto import get_random_string


class Profile(AbstractUser):

    phone = PhoneNumberField(unique=True)
    password = models.CharField(max_length=10)
    ref_code = models.CharField(default=get_random_string(8), unique=True)

    USERNAME_FIELD = "phone"
