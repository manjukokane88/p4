from django.http import HttpResponse
from django.shortcuts import render


def demo(request):
    return HttpResponse("Well come to demo page")

def index(request):
    return render(request,"index.html")

def home(request):
    return render(request,"demo/home.html")

def home1(request):
    return render(request,'demo/home1.html',context={"data":"manju","name":"rohit"})     

def home2(request):
    fruits = ['banana','mango','orange','kiwi','apple']
    return render(request,'demo/home2.html',{'fruits':fruits})  

def home3(request):
    return render(request,"demo/home3.html",{"a":15,"b":50})
