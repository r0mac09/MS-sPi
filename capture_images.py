from time import sleep
import cv2
import sys

shots = 100 # default 100 shots
if len(sys.argv) > 1:
    shots = int(sys.argv[1])

camera = cv2.VideoCapture(0)

for i in range(shots):
    return_value, image = camera.read()
    cv2.imwrite('camShot'+str(i)+'.png', image)
    print(i)
    sleep(0.2)

del(camera)

