from django.http import HttpResponse
from django.shortcuts import render


def demo(request):
    return HttpResponse("Well come to demo page")

def index(request):
    return render(request,"index.html")

def home(request):
    return render(request,"demo/home.html")