import RPi.GPIO as GPIO
import time
import sched

BLUE_LED = 40
YELLOW_LED = 33

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(BLUE_LED, GPIO.OUT)
    GPIO.setup(YELLOW_LED, GPIO.OUT)
    GPIO.output(YELLOW_LED, GPIO.HIGH)
    GPIO.output(BLUE_LED, GPIO.LOW)

def turnYellowOn():
    GPIO.output(YELLOW_LED, GPIO.HIGH)

def turnYellowOff():
    GPIO.output(YELLOW_LED, GPIO.LOW)

def turnBlueOn():
    GPIO.output(BLUE_LED, GPIO.HIGH)

def turnBlueOff():
    GPIO.output(BLUE_LED, GPIO.LOW)
    
def switchBlueOn():
    turnYellowOff()
    turnBlueOn()

def switchYellowOn():
    turnBlueOff()
    turnYellowOn()

def unlock():
    switchBlueOn()
    print('Door unlocked')

def lock():
    switchYellowOn()
    print('Door locked')

def turnLightsOn():
    raise NotImplementedError

def kill():
    turnYellowOff()
    turnBlueOff()
    GPIO.cleanup()
setup()

