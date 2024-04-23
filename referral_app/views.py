from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from rest_framework import generics
from rest_framework.response import Response

from referral_app.forms import CreateUserForm
from referral_app.models import Profile
from referral_app.serializers import ProfileSerializer


class LoginUser(LoginView):

    def get(self, request, *args, **kwargs):
        form = CreateUserForm()
        return render(
            request,
            'login.html',
            {'form': form}
        )


class ProfileFormCreateView(CreateView):

    def get(self, request, *args, **kwargs):
        form = CreateUserForm()
        return render(
            request,
            'index.html',
            {'form': form}
        )

    def post(self, request, *args, **kwargs):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            id = user.id
            return redirect(f'{id}/show/', {'user': form})

        return render(
            request, 'index.html', {'form': form}
        )


class ProfileShowView(View):

    def get(self, request, *args, **kwargs):
        print('check', kwargs)
        profile_id = kwargs.get('pk')
        profile = Profile.objects.get(id=profile_id)
        return render(
            request,
            'show.html',
            {
                'profile': profile,
            }
        )


class ProfileAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
