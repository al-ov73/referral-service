from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from app.forms import CreateUserForm
from app.models import Profile


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
        print(form)
        return render(
            request,
            'index.html',
            {'form': form}
        )

    def post(self, request, *args, **kwargs):
        form = CreateUserForm(request.POST)
        print(form)
        if form.is_valid():
            print('VALID FORM!!')
            form.save()
            # if settings.LOCAL_DEBUG:
            #     name_mail = (
            #         f'{profile.user.first_name} {profile.user.last_name}'
            #     )
            #     send_mail_to_newuser.delay(name_mail)
            #     messages.add_message(
            #         request, messages.SUCCESS,
            #         'Вам был отправлен Email'
            #     )
            messages.add_message(
                request, messages.SUCCESS,
                'User registered successfully'
            )
            return redirect('login')
        messages.add_message(
            request, messages.SUCCESS, 'Enter correct data'
        )
        return render(
            request, 'index.html', {'form': form}
        )


class ProfileShowView(View):

    def get(self, request, *args, **kwargs):
        profile_id = kwargs.get('pk')
        profile = Profile.objects.get(id=profile_id)
        return render(
            request,
            'show.html',
            {
                'profile': profile,
            }
        )