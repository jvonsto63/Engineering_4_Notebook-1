#!/usr/bin/env python3

from time import sleep
#import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
#import Adafruit_LSM303
import RPi.GPIO as GPIO
import Adafruit_BMP.BMP085 as BMP085
import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

data = []

sensor=BMP085.BMP085()

data = [0]
firstTime = True
#filename = datetime.datetime.now().strftime("Data")
filename = "file-" + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".txt"
file = open(filename, "w")
i = 0

GPIO.output(17, GPIO.LOW)

sleep(5)

GPIO.output(17, GPIO.HIGH)

while i<50:
    data[0] = sensor.read_altitude()
    data.append(sensor.read_altitude())

    #print(sensor.read_altitude())

    file.write(str(data)+str(datetime.datetime.now()))
    file.write("\n")

    if len(data) > 4:
        data[3] = data[2]
        data[2] = data[1]
        data[1] = data[0]
        del data[4]

        newavg = sum(data)/5
        if firstTime == False:
            if oldavg > newavg:
                file.write("Fake Alarm \n")

        oldavg = newavg

        firstTime = False
        i=i+1
    file.write(' Pa'.format(sensor.read_altitude()))

file.close()
print("done")

GPIO.output(17, GPIO.LOW)


    #sleep(0.01)

