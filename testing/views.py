import re
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime

def home(request):
    return HttpResponse("Hello, Django!")

def testlink(request, name):
    return render(
        request,
        'testing/testlink68.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )