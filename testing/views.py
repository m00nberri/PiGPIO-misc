from django.shortcuts import render
from .GPIOtools import toggle, cleanpins

def home(request):
    return render(request, 'testing/base.html', {})

def GPIOcontrol(request):
    return render(request, 'testing/GPIOcontrol.html', {})

def outputToggle(request, BCMnumber):
    print(f'BCMnumber is: {BCMnumber}')
    return toggle(request, BCMnumber)

def cleanup(request):
    return cleanpins(request)