from random import choices

from django import forms


#Form structure

class AdditionForm(forms.Form):

    num1=forms.IntegerField()

    num2=forms.IntegerField()

class BmiForm(forms.Form):

    w=forms.FloatField()

    h=forms.FloatField()

class SignupForm(forms.Form):

    gender_choices=(('male','Male'),('female','Female'))

    role_choices=(('admin','Admin'),('student','Student'))


    username=forms.CharField()

    password=forms.CharField(widget=forms.PasswordInput)

    place=forms.CharField()

    gender=forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)

    role=forms.ChoiceField(choices=role_choices)

    email=forms.EmailField()


class CalorieForm(forms.Form):

    level_choice=((1.2,'Sedentary'),(1.375,'Lightly Active'),(1.55,'Moderately Active'),(1.725,'Very Active'),(1.9,'Extra Active'))

    gender_choices = (('male', 'Male'), ('female', 'Female'))

    weight=forms.FloatField()

    height=forms.FloatField()

    age=forms.FloatField()

    activity_level=forms.ChoiceField(choices=level_choice)

    gender = forms.ChoiceField(choices=gender_choices, widget=forms.RadioSelect)




