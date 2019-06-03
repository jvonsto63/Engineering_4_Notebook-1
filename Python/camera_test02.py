from picamera import PiCamera
from time import sleep

myCamera = PiCamera()

myCamera.start_preview()
sleep(2)

print("Here are the effects:")
for effect in myCamera.IMAGE_EFFECTS:
    filename = "iamge_%s.jpg" % effect
    print(filename)
    myCamera.image_effect = effect
    myCamera.capture(filename)
    myCamera.annotate_text = "Candid Camera"
    sleep(1)

myCamera.stop_preview()
