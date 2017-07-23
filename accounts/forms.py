from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', required=True)
    password = forms.CharField(label='Password', required=True)

    def authenticate(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']

            return authenticate(username=username, password=password)


class RegisterForm(UserCreationForm):
    def registered(self):
        if self.is_valid():
            user = self.save()
