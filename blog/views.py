from django.shortcuts import render, HttpResponse
from .models import Hobbies, Portfolio

# Create your views here.
def greet_user(req):
   return HttpResponse("Hello World")

def home(req):
    return render(req, 'blog/home.html')

def hobbies(req):
    hobby_list=Hobbies.objects.all()
    # print(hobby_list)
    return HttpResponse(hobby_list)
    # return HttpResponse(f"<h1>hobbies</h1>\n{hobby_list}")

def portfolio(req):
    return HttpResponse(Portfolio.objects.all())

def contact(req):
    return render(req, 'blog/contact.html')
