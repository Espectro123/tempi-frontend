import RPi.GPIO as GPIO
import time
import sys

# Board pin used
PIN_SET = 12
PIN_POWER_DOWN = 8
PIN_UP = 10


def start_tk2000():
    #Choose Board mode to operate. Board is best since it support changing the RPI later on
    GPIO.setmode(GPIO.BOARD)

    # Setup de GPIO pins. We turn them down so the relay are not activated by this operation
    GPIO.setup(PIN_SET,GPIO.OUT,initial=GPIO.LOW)
    GPIO.output(PIN_SET,1)

    GPIO.setup(PIN_POWER_DOWN,GPIO.OUT,initial=GPIO.LOW)
    GPIO.output(PIN_POWER_DOWN,1)

    GPIO.setup(PIN_UP,GPIO.OUT,initial=GPIO.LOW)
    GPIO.output(PIN_UP,1)

	# Start the TK 2000
    GPIO.output(PIN_POWER_DOWN,0)
    time.sleep(3.2)
    GPIO.output(PIN_POWER_DOWN,1)
    GPIO.cleanup()

def set_started_temperature():
	#Choose Board mode to operate. Board is best since it support changing the RPI later on
    GPIO.setmode(GPIO.BOARD)

    # Setup de GPIO pins. We turn them down so the relay are not activated by this operation
    GPIO.setup(PIN_SET,GPIO.OUT,initial=GPIO.LOW)
    GPIO.output(PIN_SET,1)

    GPIO.setup(PIN_POWER_DOWN,GPIO.OUT,initial=GPIO.LOW)
    GPIO.output(PIN_POWER_DOWN,1)

    GPIO.setup(PIN_UP,GPIO.OUT,initial=GPIO.LOW)
    GPIO.output(PIN_UP,1)
    
	# Enter TEMPERATURE SET MODE
    GPIO.output(PIN_SET,0)
    time.sleep(3.2)
    GPIO.output(PIN_SET,1)
    time.sleep(1)
    
    # SET STARTED TEMPERATURE TO MAX 30ºC
    GPIO.output(PIN_UP,0)
    time.sleep(10)
    GPIO.output(PIN_UP,1)
    time.sleep(1)
    
    # Exit set mode
    GPIO.output(PIN_SET,0)
    time.sleep(0.2)
    GPIO.output(PIN_SET,1)
    time.sleep(1)
    
    
    GPIO.cleanup()
