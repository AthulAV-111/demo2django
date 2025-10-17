from lib2to3.fixes.fix_input import context

from django.db.models.fields import return_None
from django.shortcuts import render

from app1.forms import AdditionForm

from app1.forms import BmiForm


from app1.forms import SignupForm
from django.template.context_processors import request

from app1.forms import CalorieForm


# Create your views here.

def addition(request):
    if(request.method=="POST"):
        print(request.POST)#submitted data
        #createing form_instance using submited data
        form_instance=AdditionForm(request.POST)
        #check whether the data is valid
        if form_instance.is_valid():

            #process data
            data=form_instance.cleaned_data  #valid data
            print(data)
            n1=data['num1']
            n2=data['num2']
            s=int(n1)+int(n2)
            context={'result':s,'form':form_instance}


            return render(request,'addition.html',context)

    if(request.method=="GET"):
        form_instance=AdditionForm()  #empty form object
        context={'form':form_instance}
        return render(request,'addition.html',context)


def factorial(request):
    if(request.method=="POST"):
        print(request.POST)
        a=int(request.POST['f'])
        fact=1
        for i in range(1,a+1):
            fact=fact*i

        context={'result':fact}

        return render(request,'factorial.html',context)

    if (request.method == "GET"):
        return render(request, 'factorial.html')



def bmi(request):
    if(request.method=="POST"):
        print(request.POST)
        form_instance=BmiForm(request.POST)
        if form_instance.is_valid():
            # process data
            data =form_instance.cleaned_data  # valid data
            print(data)
            n1 = float(data['w'])
            n2 = float(data['h'])
            s = (n1/(n2**2))
            context = {'result': s, 'form': form_instance}

            return render(request, 'bmi.html', context)





    if(request.method=="GET"):
        form_instance=BmiForm()
        context={'form':form_instance}
        return render(request,'bmi.html',context)


def signup(request):
    if(request.method=="POST"):
        print(request.POST)
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            data = form_instance.cleaned_data
            print(data)
            context={'form':form_instance}
            return render(request,'signup.html',context)


    if(request.method=="GET"):
        form_instance=SignupForm()
        context={'form':form_instance}
        return render(request, 'signup.html',context)




def calorie(request):
    if(request.method=="POST"):
        form_instance=CalorieForm(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            print(data)
            w=float(data['weight'])
            h=float(data['height'])
            a=float(data['age'])
            g=data['gender']
            l=float(data['activity_level'])

            if(g=='male'):
                bmr=(10*w+6.25*h-5*a+ 5) #male
            else:
                bmr = (10 * w + 6.25 * h - 5 * a -161)  #female

            print("BMR=",bmr)
            c=bmr*l
            print("Calorie=",c)
            context={'result':c, 'form':form_instance}
            return render(request,'calorie.html',context)


    if(request.method=="GET"):
        form_instance=CalorieForm()
        context={'form':form_instance}
        return render(request,'calorie.html',context)





