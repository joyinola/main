from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def damy(request):
	return HttpResponse("hello, damy")

def greet(request,name):
	return render(request,"hello/greet.html", {'name':name.capitalize()})

def index(request):
	return render(request,"hello/index.html")