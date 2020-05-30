from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(
        "Hello, world. I really don't know what am doing yet if he says so."
    )


def moew(request):
    return HttpResponse("i still dont know what am doing.")
