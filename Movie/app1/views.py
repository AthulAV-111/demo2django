from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect

from app1.forms import MovieForm

from .models import Moviedetails
# Create your views here.

def Movielist(request):
    a = Moviedetails.objects.all()
    context = {'details': a}

    return render(request,'Movielist.html',context)





def addmovies(request):
    if(request.method=="POST"):# after submission
        form_instance=MovieForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('app1:Movielist')



    if (request.method=="GET"):
        form_instance=MovieForm()
        context={'form':form_instance}
        return render(request,'addmovies.html',context)


def moviedetail(request,i):
    if(request.method=="GET"):
        a=Moviedetails.objects.get(id=i)
        context={'movie':a}

        return render(request,'moviedetail.html',context)

def movieedit(request,i):
    if (request.method == "POST"):  # after submission
        a = Moviedetails.objects.get(id=i)
        form_instance = MovieForm(request.POST, request.FILES,instance=a)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('app1:Movielist')


    if(request.method=="GET"):
        a=Moviedetails.objects.get(id=i)
        form_instance=MovieForm(instance=a)
        context={'form':form_instance}
        return render(request,'movieedit.html',context)

def moviedelete(request,i):
    a = Moviedetails.objects.get(id=i)
    a.delete()
    return redirect('app1:Movielist')




