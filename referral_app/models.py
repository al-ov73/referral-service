from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.crypto import get_random_string


class ProfileManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone, password, **kwargs):
        if not phone:
            raise ValueError('Users require an phone field')
        user = self.model(phone=phone, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(phone, password, **kwargs)


class Profile(AbstractUser):
    username = None
    phone = PhoneNumberField(unique=True)
    ref_code = models.CharField(default=get_random_string(8), unique=True)

    objects = ProfileManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone

class ReferralRegistry(models.Model):
    in_id = models.IntegerField()
    out_id = models.IntegerField(unique=True)