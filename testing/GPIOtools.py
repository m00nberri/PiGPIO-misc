import RPi.GPIO as GPIO
from django.http import HttpResponse
from django.shortcuts import redirect

useablePins = {3,4,17,27,22,5,6,13,26,23,24,25,12,16}

def turnOn(BCMnumber):
    GPIO.setmode(GPIO.BCM)
    GPIO.output(BCMnumber, 1)
    return

def turnOff(BCMnumber):
    GPIO.setmode(GPIO.BCM)
    GPIO.output(BCMnumber, 0)
    return

def toggle(request, BCMnumber):
    GPIO.setmode(GPIO.BCM)
    pin = BCMnumber
    pinmode = GPIO.gpio_function(pin)
    print(f'Pin is: {pin} and its mode is {pinmode}')
    if pinmode == 1:
        switchOut(pin)
        turnOn(pin)
        return redirect('GPIOcontrol')
    elif pinmode == 0:
        if GPIO.input(pin):
            turnOff(pin)
            return redirect('GPIOcontrol')
        else:
            turnOn(pin)
            return redirect('GPIOcontrol')
    else:
        return redirect('GPIOcontrol')

def switchOut(BCMnumber):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BCMnumber,GPIO.OUT)
    GPIO.output(BCMnumber, 0)
    return

def cleanpins(request):
    GPIO.setmode(GPIO.BCM)
    for pin in useablePins:
        try:
            GPIO.setup(pin, GPIO.IN)
        except Exception as e:
            print(f'idkwhathappun at pin: {pin} Exception: {e}')
    return redirect('GPIOcontrol')