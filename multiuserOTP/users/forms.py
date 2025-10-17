
from django.contrib.auth.models import  User
from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser



class SignupForm(UserCreationForm):
    role_choices=(('student','Student'),('teacher','Teacher'))
    role=forms.ChoiceField(choices=role_choices)

    gender_choices = (('male', 'Male'), ('female', 'Female'))
    gender = forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)

    class Meta:
        model=CustomUser
        fields=['username','password1','password2','email','first_name','last_name','phone','role','gender']


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

#
# class OtpForm(forms.Form):
#     enter_otp=forms.CharField(max_length=30)



