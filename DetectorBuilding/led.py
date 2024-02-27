import RPi.GPIO as GPIO
from time import sleep

class led:
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(14, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
        
    def multiLED (self,val):
        GPIO.output(14,GPIO.LOW)
        GPIO.output(15,GPIO.LOW)
        GPIO.output(18,GPIO.LOW)
        if (val > 0 and val < 100):
            GPIO.output(14,GPIO.HIGH)
        elif (val >= 100 and val < 200):
            GPIO.output(15,GPIO.HIGH)
        elif (val >= 200 and val < 300):
            GPIO.output(18,GPIO.HIGH)
        elif (val >= 300 and val < 400):
            GPIO.output(14,GPIO.HIGH)
            GPIO.output(15,GPIO.HIGH)
        elif (val >= 400 and val < 500):
            GPIO.output(14,GPIO.HIGH)
            GPIO.output(18,GPIO.HIGH)
        elif (val >= 500 and val < 600):
            GPIO.output(15,GPIO.HIGH)
            GPIO.output(18,GPIO.HIGH)
        elif (val >= 600):
            GPIO.output(14,GPIO.HIGH)
            GPIO.output(15,GPIO.HIGH)
            GPIO.output(18,GPIO.HIGH)
