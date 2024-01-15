import RPi.GPIO as GPIO
import time
import sys
from app.utils.read_temperature import read_temperature

# Board pin used
PIN_SET = 12
PIN_POWER_DOWN = 8
PIN_UP = 10

# Turns down the TK 2000
def turn_down_tk2000():
    #Choose Board mode to operate. Board is best since it support changing the RPI later on
    GPIO.setmode(GPIO.BOARD)

    # Setup de GPIO pins. We turn them down so the relay are not activated by this operation
    GPIO.setup(PIN_SET,GPIO.OUT,initial=GPIO.LOW)
    GPIO.output(PIN_SET,1)

    GPIO.setup(PIN_POWER_DOWN,GPIO.OUT,initial=GPIO.LOW)
    GPIO.output(PIN_POWER_DOWN,1)

    GPIO.setup(PIN_UP,GPIO.OUT,initial=GPIO.LOW)
    GPIO.output(PIN_UP,1)
    
    GPIO.output(PIN_POWER_DOWN,1)
    time.sleep(3.2)
    GPIO.output(PIN_POWER_DOWN,0)
    time.sleep(1)

# Set a temperature in the TK 2000
def set_temperature(current_temperature,new_temperature):
    current_temperature = float(current_temperature)
    new_temperature = float(new_temperature)
    print("Set temperature called with parameters: Current temperature: ", current_temperature, " and New temperature: ", new_temperature)
    
    #Choose Board mode to operate. Board is best since it support changing the RPI later on
    GPIO.setmode(GPIO.BOARD)

    # Setup de GPIO pins. We turn them down so the relay are not activated by this operation
    GPIO.setup(PIN_SET,GPIO.OUT,initial=GPIO.LOW)
    GPIO.output(PIN_SET,1)

    GPIO.setup(PIN_POWER_DOWN,GPIO.OUT,initial=GPIO.LOW)
    GPIO.output(PIN_POWER_DOWN,1)

    GPIO.setup(PIN_UP,GPIO.OUT,initial=GPIO.LOW)
    GPIO.output(PIN_UP,1)
    
    # Enter set mode
    
    GPIO.output(PIN_SET,0)
    time.sleep(3.1) # We wait a bit more than 3 seconds
    GPIO.output(PIN_SET,1)
    
    if current_temperature > new_temperature:
        # We need to lower the temperature
        temperature_clicks = (current_temperature - new_temperature)*10
        while temperature_clicks >= 0:
            temperature_clicks = temperature_clicks - 1
            # Turn down temperature by 0.1 degrees
            GPIO.output(PIN_POWER_DOWN,0)
            time.sleep(0.1)
            GPIO.output(PIN_POWER_DOWN,1)
            time.sleep(0.1)
            
    elif current_temperature < new_temperature:
        # We need to raise the temperature
        temperature_clicks = (new_temperature - current_temperature)*10
        while temperature_clicks >= 0:
            temperature_clicks = temperature_clicks -1
            # Raise temperature by 0.1 degrees
            GPIO.output(PIN_UP,0)
            time.sleep(0.1)
            GPIO.output(PIN_UP,1)
            time.sleep(0.1)
    
    # Exit set mode
    GPIO.output(PIN_SET,0)
    time.sleep(0.2)
    GPIO.output(PIN_SET,1)
    
    GPIO.cleanup()
