from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# localhost:8080/demo/hello

# def say_hello(request):
#     return HttpResponse("Welcome to my app")
# return render(request, 'index.html', context={'name': })


def welcome(request, name):
    return render(request, 'index.html', context={'name': name})


def say_hello(request):
    return HttpResponse("Welcome to Django")
