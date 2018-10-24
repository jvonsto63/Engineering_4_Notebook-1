import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

counter = 0
while(counter <= 10):
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(18, GPIO.HIGH)
    sleep(1)

    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    sleep(1)

    counter =+ 1
