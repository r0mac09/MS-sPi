import RPi.GPIO as GPIO
import time

BLUE_LED = 40
YELLOW_LED = 33

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(BLUE_LED, GPIO.OUT)
    GPIO.setup(YELLOW_LED, GPIO.OUT)
    GPIO.output(YELLOW_LED, GPIO.LOW)
    GPIO.output(BLUE_LED, GPIO.LOW)

def turnYellowOn():
    GPIO.output(YELLOW_LED, GPIO.HIGH)

def turnYellowOff():
    GPIO.output(YELLOW_LED, GPIO.LOW)

def turnBlueOn():
    GPIO.output(BLUE_LED, GPIO.HIGH)

def turnBlueOff():
    GPIO.output(BLUE_LED, GPIO.LOW)
    
def unlock():
    print('Door unlocked')

def lock():
    print('Door locked')

setup()

