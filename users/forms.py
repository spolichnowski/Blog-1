from django import forms

from .models import User


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(label='Imie', max_length=25)
    last_name = forms.CharField(label='Nazwisko', max_length=35)
    email = forms.EmailField(max_length=255)
    password = forms.CharField(
        label='Hasło',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Powtórz hasło',
        widget=forms.PasswordInput
    )


    def cleaned_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise forms.ValidationError('Podane hasłą są inne.Spróbuj ponownie.')
        return password2
