from django.shortcuts import render

# Create your views here.

def addition(request):
    if(request.method=="POST"):
        print(request.POST)
        n1=int(request.POST['n1'])
        n2=int(request.POST['n2'])
        s=n1+n2

        context={'result':s}

        return render(request, 'addition.html',context)

    if(request.method=="GET"):
        return render(request,'addition.html')


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
        w = int(request.POST['w'])
        h = int(request.POST['h'])
        b=w/(h*h)


        context = {'result': b}

        return render(request,'bmi.html',context)



    if(request.method=="GET"):
        return render(request,'bmi.html')






