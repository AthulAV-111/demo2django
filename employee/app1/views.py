from django.shortcuts import render, redirect

from app1.forms import employeeform

from app1.models import employee

# Create your views here.



def create(request):
    if(request.method=="POST"):
        form_instance=employeeform(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()

            return redirect('app1:read')



    if(request.method=="GET"):
        form_instance=employeeform()
        context={'form':form_instance}
        return render(request,'create.html',context)


def read(request):
    e=employee.objects.all()

    context={'app1':e}
    return render(request,'read.html',context)
