
from books.models import Book

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

from django import forms

class SignupForm(UserCreationForm):
    class Meta:
        model =User
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name']

#
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
