from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, goat. goat is better than meow khalifah, just so u know.")

