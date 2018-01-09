import cv2
import time
import numpy as np

camera = cv2.VideoCapture("rtsp://192.168.1.10:554/user=admin_password=admin_channel=1_stream=0.sdp?real_stream")
time.sleep(1.0)

i = 0
while True:
    ret, frame = camera.read()
    if ret == False:
        print('Failed to capture frame from camera. Check camera index in cv2.VideoCapture(0) \n')
        break
    cv2.imwrite('imgs2/pic{:>05}.jpg'.format(i), frame)        
    i=i+1
    cv2.imshow("frame",frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break