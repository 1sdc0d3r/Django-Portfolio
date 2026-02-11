from django.shortcuts import render, HttpResponse


# Create your views here.
def greet_user(req):
   return HttpResponse("Hello World")

def home(req):
    return HttpResponse("Home")

def hobbies(req):
    return HttpResponse("hobbies")

def portfolio(req):
    return HttpResponse("portfolio")

def contact(req):
    return HttpResponse("contact")
