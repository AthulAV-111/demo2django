from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.


#Home View
def Home(request):
    return HttpResponse("welcome to new django app")


#index view

def Index(request):
    return HttpResponse("Index page")



