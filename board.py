import RPi.GPIO as GPIO
import time

BLUE_LED = 40
YELLOW_LED = 33

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(BLUE_LED, GPIO.OUT)
    GPIO.setup(YELLOW_LED, GPIO.OUT)
    GPIO.output(YELLOW_LED, GPIO.HIGH)
    GPIO.output(BLUE_LED, GPIO.HIGH)
