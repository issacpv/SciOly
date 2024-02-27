import spidev
import time
import numpy as np
import RPi.GPIO as GPIO
import LCDx16
from led import led

oLED = led()
lcd = LCDx16.lcd16()
delay = 0.5
e = 2.718281828
GPIO.setmode(GPIO.BCM)

#open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

#define custom chip select
CS_ADC = 22
GPIO.setup(CS_ADC, GPIO.OUT)

#function to read data from MCP3008 chip
def ReadChannel3008(channel=0):
    #send 0000001 1xxx0000 0000000 to the chip and records the response
    #xxx encodeds 0-7, the channel selected for the transfer
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

def ConvertToVoltage(value, bitdepth, vref):
    return vref*(value/(2**bitdepth-1))

def CleanAndExit():
    print("cleaning...")
    GPIO.cleanup()
    print ("Bye")
    sys.exist()

while True:
    try:
        GPIO.output(CS_ADC, GPIO.LOW)
        time.sleep(.5)
        value = ReadChannel3008(0)
        GPIO.output(CS_ADC, GPIO.HIGH)
        time.sleep(.5)
        voltage = ConvertToVoltage(value,10,3.3) #for MCP30 value = (1.004350935 ** value) * 37.9933612
        value = 2382.55973282 / (1 + (54.726354287274 * (e ** (-.0045081215870084 * value))))
        print(f"Voltage:{voltage:.6f} Value:{value}")
        lcd.lcd_string("Weight: " + str(value),lcd.LCD_LINE_1)
        lcd.lcd_string("Voltage: " + str(voltage),lcd.LCD_LINE_2)
        oLED.multiLED(value)
        time.sleep(delay)
    
    except (KeyboardInterrupt, SystemExit):
            CleanAndExist()
