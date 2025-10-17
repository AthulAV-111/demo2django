from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



def register(request):
    return render(request,'register.html')




def Login(request):
    return render(request,'Login.html')



def logout(request):
    return HttpResponse("Logout")

