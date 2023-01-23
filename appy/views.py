from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def chase(request):
    return HttpResponse("Hello Chase")

def daniel(request):
    return HttpResponse("hey Daniel")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })