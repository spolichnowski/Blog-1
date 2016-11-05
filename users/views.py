from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import User

from .forms import LoginForm, UserRegistrationForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd['email'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Pomyślnie zalogowany')
                else:
                    return HttpResponse('Konto nieaktywne')
            else:
                return HttpResponse('Użytkownik nie istnieje')
    else:
        form = LoginForm()
    return render(request,
                  'users/login.html',
                  {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            cd = user_form.cleaned_data
            password = cd.get('password')
            first_name = cd.get('first_name')
            last_name = cd.get('last_name')
            email = cd.get('email')
            new_user = User(
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            new_user.set_password(password)
            new_user.save()

            reply = {
                'subject': 'Dziękujemy za rejestrację.',
                'message': 'Zarejestrowałeś się w naszym portalu.'
            }

            new_user.return_message(reply)
            return render(request,
                          'users/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'users/register.html',
                  {'user_form': user_form})
