import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
mode = GPIO.getmode()

GPIO.setup(11, GPIO.OUT)

i = 0
try:
    while True: 
        GPIO.output(11,1)
        sleep(0.05)
        GPIO.output(11,0)
        sleep(0.05)
        print(f'flash {i}')
        i += 1

except KeyboardInterrupt:
    GPIO.cleanup()