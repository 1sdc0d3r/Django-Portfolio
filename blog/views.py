from django.shortcuts import render, HttpResponse


# Create your views here.
def greet_user(req):
   return HttpResponse("Hello World")

def home(req):
    return HttpResponse(f'''<div style='padding:2em;'><p>
                I am an avid fisherman with a passion to develop software. As
                technology evolves, we must learn to evolve with it. This is
                prominent for a successful future.
              </p>
              <p>
                Change is inevitable, there will always be something that is
                going to try to hold you back. When there is a new problem, I
                find a new solution. This is the only way to progress.
              </p>
            <p>
              Today is a new day.
              <br />I love being a source of color in a binary world!
            </p>
            </div>''')

def hobbies(req):
    return HttpResponse("hobbies")

def portfolio(req):
    return HttpResponse("portfolio")

def contact(req):
    return HttpResponse("bradenbell@mail.weber.edu")
