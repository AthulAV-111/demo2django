from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect

from books.forms import BookForm

from books.models import Book

from django.template.defaultfilters import title

from django.views import View




# Create your views here.
#
# def homeview(request):
#     return render(request,'homeview.html')


class Home(View):
    def get(self,request):
        return render(request, 'homeview.html')


# def addbooks(request):
#     return render(request,'addbooks.html')

class Addbooks(View):
    def get(self,request):
        form_instance = BookForm()
        context = {'form': form_instance}
        return render(request, 'addbooks.html', context)

    def post(self,request):
        form_instance = BookForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('books:viewbooks')

#
# def addbooks(request):
#     if(request.method=="POST"):
#
#         form_instance=BookForm(request.POST,request.FILES)
#         if form_instance.is_valid():
#             form_instance.save()
#             # data = form_instance.cleaned_data
            # print(data)
            # t=data['title']
            # a=data['author']
            # p=data['price']
            # pg=data['pages']
            # l=data['language']
            # b=Book.objects.create(title=t,author=a,price=p,pages=pg,language=l)
            # b.save()

            # return redirect('books:viewbooks')
            # return render(request, 'addbooks.html')


    #
    # if(request.method=="GET"):
    #     form_instance=BookForm()
    #     context={'form':form_instance}
    #     return render(request, 'addbooks.html',context)
    #

class Viewbooks(View):
    def get(self,request):
        b = Book.objects.all()  # to read all records from table

        context = {'books': b}
        return render(request, 'viewbooks.html', context)

#
# def viewbooks(request):
#     b=Book.objects.all()  #to read all records from table
#
#     context={'books':b}
#     return render(request,'viewbooks.html',context)


class Bookdetail(View):
    def get(self,request,i):
        b = Book.objects.get(id=i)
        context = {'book': b}

        return render(request, 'bookdetail.html', context)

#
# def bookdetail(request,i):
#     if(request.method=="GET"):
#
#         b=Book.objects.get(id=i)
#         context={'book':b}
#
#         return render(request,'bookdetail.html',context)

class Editbook(View):
    def get(self,request,i):
        b = Book.objects.get(id=i)
        form_instance = BookForm(instance=b)
        context = {'form': form_instance}
        return render(request, 'editbook.html', context)


    def post(self,request,i):
        if (request.method == "POST"):
            b = Book.objects.get(id=i)

            form_instance = BookForm(request.POST, request.FILES, instance=b)
            if form_instance.is_valid():
                form_instance.save()
                return redirect('books:viewbooks')

#
# def editbook(request,i):
#     if (request.method == "POST"):
#         b = Book.objects.get(id=i)
#
#         form_instance = BookForm(request.POST, request.FILES,instance=b)
#         if form_instance.is_valid():
#             form_instance.save()
#             return redirect('books:viewbooks')
#
#     if(request.method=="GET"):
#         b=Book.objects.get(id=i)
#         form_instance=BookForm(instance=b)
#         context={'form':form_instance}
#         return render(request,'editbook.html',context)
#

class Deletebook(View):
    def get(self,request,i):
        b = Book.objects.get(id=i)
        b.delete()
        return redirect('books:viewbooks')

# def deletebook(request,i):
#     b=Book.objects.get(id=i)
#     b.delete()
#     return redirect('books:viewbooks')
#


from django.db.models import Q

class Search(View):
    def get(self,request):
        query=request.GET['q']

        if query:
            b=Book.objects.filter(Q(author__icontains=query)|Q(title__icontains=query)|Q(language__icontains=query))
            #Q object - syntax used to add logical or/and in ORM queries
            #field lookups -fieldname__lookup eg:age__gt=30/age__lt=30/title__contains=/title__icontains=

            context={'book':b}

            return render(request, 'search.html',context)






