from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#
# #Fiest view
#
# def First(request):
#     return HttpResponse("First page")
#
#
# #Second view
#
# def Second(request):
#     return HttpResponse("Second page")





def First(request):
    context={'name':'arun','age':23} #context - is dictionary type
                                     # is used to pass data from views to html page

    return render(request,'first.html',context)


#Second view

def Second(request):
    context={'name':'amal','age':28}
    return render(request,'second.html',context)
