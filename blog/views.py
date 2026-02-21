from django.shortcuts import render, HttpResponse
from .models import Hobbies, Portfolio

# Create your views here.
def greet_user(req):
   return HttpResponse("Hello World")

def home(req):
    return render(req, 'blog/home.html')

def hobbies(req):
    hobby_list = Hobbies.objects.all()
    context = {'hobbies': hobby_list}
    return render(req, 'blog/hobbies.html', context)


def hobby_detail(req, id):
    item = Hobbies.objects.get(pk=id)
    context = {'hobby': item}
    return render(req, 'blog/hobby_detail.html', context)


def portfolio(req):
    portfolio_list = Portfolio.objects.all()
    context = {'portfolios': portfolio_list}
    return render(req, 'blog/portfolio.html', context)


def portfolio_detail(req, id):
    item = Portfolio.objects.get(pk=id)
    context = {'portfolio': item}
    return render(req, 'blog/portfolio_detail.html', context)

def contact(req):
    return render(req, 'blog/contact.html')
