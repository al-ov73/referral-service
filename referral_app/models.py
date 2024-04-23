from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
#
# User = get_user_model()
#

class Profile(AbstractUser):
    phone = PhoneNumberField(unique=True)
    ref_code = models.CharField(default=get_random_string(8), unique=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone
