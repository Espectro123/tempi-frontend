import RPi.GPIO as GPIO
import time
import sys
import read_temperature

# Board pin used
PIN_SET = 12
PIN_POWER_DOWN = 8
PIN_UP = 10

# Short pulse should be 0.2 seconds
# Large pulse should be 3 seconds
def pulse(pin,seconds):
    GPIO.output(pin,0)
    time.sleep(seconds)
    GPIO.output(pin,1)

def turn_down_pin_at_setup(pin):
    GPIO.output(pin,1)


def set_temperature(initial_temperature,expected_temperature):

    action = ""

    # We want to cool the water
    if initial_temperature > expected_temperature:
        action = "cool"
        pulse(PIN_SET,3) # Necesary to enter setup mode on the machine

    # We want to heat
    elif initial_temperature < expected_temperature:
        action = "heat"
        pulse(PIN_SET,3)

    # We want to do nothing
    elif initial_temperature == expected_temperature:
        action = "none"
    
    else:
        print("ERROR on control_tk2000.py")
        exit()

    while initial_temperature != expected_temperature:
        if action == "cool":
            pulse(PIN_POWER_DOWN,0.2)
            initial_temperature = float(initial_temperature - 0.1)
        elif action == "heat":
            pulse(PIN_UP,0.2)
            initial_temperature = float(initial_temperature + 0.1)

    # Para terminar pulsamos el boton set
    pulse(PIN_SET,0.2)

def turn_on_off_tank():
    pulse(PIN_POWER_DOWN,3)

# Main method
# action -> String
# initial_temperature -> float
# expected_temperature -> float
def control_tk(action,initial_temperature,expected_temperature):
    #Choose Board mode to operate. Board is best since it support changing the RPI later on
    GPIO.setmode(GPIO.BOARD)

    # Setup de GPIO pins. We turn them down so the relay are not activated by this operation
    GPIO.setup(PIN_SET,GPIO.OUT,initial=GPIO.LOW)
    turn_down_pin_at_setup(PIN_SET)

    GPIO.setup(PIN_POWER_DOWN,GPIO.OUT,initial=GPIO.LOW)
    turn_down_pin_at_setup(PIN_POWER_DOWN)

    GPIO.setup(PIN_UP,GPIO.OUT,initial=GPIO.LOW)
    turn_down_pin_at_setup(PIN_UP)

    if action == "TurnOn" or action == "TurnOff":
        turn_on_off_tank()
    elif action == "SetUpTemperature":
        set_temperature(initial_temperature,expected_temperature)
    else:
        print("Action not recognize on script control_tk2000.py")
        exit()
    
    GPIO.cleanup()


# Parameters
# Action: SetUpTemperature, TurnOff, TurnOn
# InitialTemperature
# ExpectedTemperature
