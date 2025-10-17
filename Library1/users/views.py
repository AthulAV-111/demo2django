from django.http import HttpResponse
from django.shortcuts import render,redirect

from users.forms import SignupForm

from django.views import View

from users.forms import LoginForm

from django.contrib.auth import authenticate,login,logout

from django.contrib import messages

# Create your views here.


class Register(View):
    def get(self, request):
        form_instance = SignupForm()
        context = {'form': form_instance}
        return render(request, 'register.html', context)

    def post(self, request):
        form_instance = SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('users:Login')
        else:
            print('error')
            return render(request, 'register.html', {'form': form_instance})


class Userlogin(View):

    def get(self, request):
        form_instance = LoginForm()
        context = {'form': form_instance}
        return render(request, 'login.html', context)

    def post(self, request):
        form_instance = LoginForm(request.POST)
        if (form_instance.is_valid()):
            u = form_instance.cleaned_data['username']
            p = form_instance.cleaned_data['password']
            user = authenticate(username=u, password=p)
            # authenticate() returns user object if user with the given username and password exists
            # else return none

            if user:  # is user exists
                login(request, user)  # login()adds the current user into session
                return redirect('books:homeview')
            else:
                messages.error(request, 'invalid user credentials')
                return render(request, 'login.html', {'form': form_instance})


class Userlogout(View):
    def get(self, request):
        logout(request)
        return redirect('users:Login')




