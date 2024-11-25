from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from .models import Person
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

#Create your views here.
def fun(request):
    return HttpResponse("<h1> students </h1>")
def index(request):
    return HttpResponse("Hello world, This is my first django project")

def my_view(request):
    a={"title":"python"}
    return render(request,'index.html',a)

def list(request):
    a=[10,20,30,40,50]
    dict={"list":a}
    return render(request,"list.html",dict)

def form(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        return HttpResponse(f"Received username: {username}, received email: {email}")
    return render(request,'form.html')

def add_db(request):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        Person.objects.create(name=name,age=age)
        return HttpResponseRedirect('/success')
    return render(request, 'add_db.html')
def success(request):
    Persons=Person.objects.all()
    print(Persons)
    return render(request,"success.html",{"persons":Persons})

def fun4(request):
    a=100
    return HttpResponse(a)

def fun5(request):
    new=fun4(request)
    return HttpResponse(new)

def delete(request,pername,perage):
    pers=Person.objects.get(name=pername)
    pers.delete()
    return HttpResponseRedirect("/success")

def update(request,pername,perage):
    person=Person.objects.get(name=pername)
    if request.method=="POST":
        newname=request.POST.get("name")
        newage=request.POST.get("age")
        person.name=newname
        person.age=newage
        person.save()
        return redirect("/success")
    return render(request,"update.html",{"person":person})

class ItemViewSet(viewsets.ModelViewSet):
    queryset=Item.objects.all()
    serializer_class=ItemSerializer

