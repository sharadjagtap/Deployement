from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import datetime

def time_info(request):
    time=datetime.datetime.now()
    s="Hello current time is "+str(time)
    return HttpResponse(s)


