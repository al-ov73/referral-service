from django.contrib.auth.forms import (
    UserCreationForm,
)
from django import forms
from django.forms import ModelForm
from referral_app.models import Profile


class CreateUserForm(UserCreationForm):

    class Meta:

        model = Profile
        fields = [
            'phone',
        ]
