import RPi.GPIO as GPIO
import time
import sched

from logger import log

BLUE_LED = 40
YELLOW_LED = 33
LOCKED = True

def setup():
    global BLUE_LED
    global YELLOW_LED
    global LOCKED
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(BLUE_LED, GPIO.OUT)
    GPIO.setup(YELLOW_LED, GPIO.OUT)
    GPIO.output(YELLOW_LED, GPIO.HIGH)
    GPIO.output(BLUE_LED, GPIO.LOW)

def turnYellowOn():
    global YELLOW_LED
    GPIO.output(YELLOW_LED, GPIO.HIGH)

def turnYellowOff():
    global YELLOW_LED
    GPIO.output(YELLOW_LED, GPIO.LOW)

def turnBlueOn():
    global BLUE_LED
    GPIO.output(BLUE_LED, GPIO.HIGH)

def turnBlueOff():
    global BLUE_LED
    GPIO.output(BLUE_LED, GPIO.LOW)
    
def switchBlueOn():
    turnYellowOff()
    turnBlueOn()

def switchYellowOn():
    turnBlueOff()
    turnYellowOn()

# it should switch the lock into open position
def unlock():
    global LOCKED
    if LOCKED:
        switchBlueOn()
        LOCKED = False
        log('Door unlocked')
        time.sleep(5)

# it should put the locked into locked position
def lock():
    global LOCKED
    if not LOCKED:
        switchYellowOn()
        LOCKED = True
        log('Door locked')

def turnLightsOn():
    raise NotImplementedError

def kill():
    turnYellowOff()
    turnBlueOff()
    GPIO.cleanup()
    log('Raspberry functionality is shut down ...')
