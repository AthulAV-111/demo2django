
# Create your views here.

from django.contrib.auth import login, logout

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate

from django.views import View
from pyexpat.errors import messages
from django.contrib import messages
from users.forms import SignupForm
from users.forms import LoginForm



from django.contrib.auth.forms import UserCreationForm

class Home(View):
    def get(self,request):
        return render(request,'home.html')


class Adminhome(View):
    def get(self,request):
        return render(request,'adminhome.html')


class Studenthome(View):
    def get(self,request):
        return render(request,'studenthome.html')


class Teacherhome(View):
    def get(self,request):
        return render(request,'teacherhome.html')

class Register(View):
    def get(self,request):
        form_instance=SignupForm()
        context={'form':form_instance}
        return render(request,'register.html',context)

    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('users:login')
        else:
            print('error')
            return render(request,'register.html',{'form':form_instance})


class Userlogin(View):
    def get(self,request):
        form_instance = LoginForm()
        context = {'form': form_instance}
        return render(request,'login.html',context)

    def post(self,request):
        form_instance=LoginForm(request.POST)
        if(form_instance.is_valid()):
            u=form_instance.cleaned_data['username']
            p=form_instance.cleaned_data['password']
            user=authenticate(username=u,password=p)
            #authenticate() returns user object if user with the given username and password exists
            #else return none

            if user and user.is_superuser==True:#is user is admin
                login(request, user)#login()adds the current user into session
                return redirect('users:adminhome')
            elif user and user.role=='student':#if user is student
                login(request, user)  # login()adds the current user into session
                return redirect('users:studenthome')
            elif user and user.role == 'teacher':#if user is teacher
                login(request, user)  # login()adds the current user into session
                return redirect('users:teacherhome')


            else:
                messages.error(request,'invalid user credentials')
                return render(request, 'login.html', {'form': form_instance})


class Userlogout(View):
    def get(self,request):
        logout(request)
        return redirect('users:login')





