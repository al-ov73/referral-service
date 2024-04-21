from django.contrib.auth.forms import (
    UserCreationForm,
)
from django import forms

from app.models import Profile


class CreateUserForm(UserCreationForm):

    class Meta:

        model = Profile
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = [
            'phone',
            'password1',
            'password2',
        ]
