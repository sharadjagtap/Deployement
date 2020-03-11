from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def good_morning(request):
    return HttpResponse ("Hello good morning...")


def good_afternoon(request):
    return HttpResponse("Hello good afternoon")


def good_evening(request):
    return HttpResponse("Good Evening")