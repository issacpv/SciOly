import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(17,GPIO.OUT)
servo1 = GPIO.PWM(7,50) # Note 11 is pin, 50 = 50Hz pulse
servo1.start(0)
GPIO.setup(12,GPIO.OUT)
servo1 = GPIO.PWM(12,50) # Note 11 is pin, 50 = 50Hz pulse
servo1.start(0)

servo1.ChangeDutyCycle(12)
time.sleep(1)

#Clean things up at the end
servo1.stop()
GPIO.cleanup()
print ("Goodbye")