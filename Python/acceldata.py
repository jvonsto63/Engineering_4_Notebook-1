import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

lsm303 = Adafruit_LSM303.LSM303()

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)


disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height), outline=0, fill=0)

padding = 2
shape_width = 20
top = padding
bottom = height-padding
x = padding

font = ImageFont.load_default()

while True:
    accel, mag = lsm303.read()
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag

    accel_x /= 100
    accel_y /= 100
    accel_z /= 100

    draw = ImageDraw.Draw(image)
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    draw.text((x, top),    'ACCEL DATA:',  font=font, fill=255)
    draw.text((x, top+20), 'X: ' + str(accel_x), font=font, fill=255)
    draw.text((x, top+30), 'Y: ' + str(accel_y), font=font, fill=255)
    draw.text((x, top+40), 'Z: ' + str(accel_z), font=font, fill=255)

    disp.image(image)
    disp.display()
