from django.shortcuts import render

def home(request):
    title = 'Pi Stuff'
    return render(request, 'testing/base.html', {})