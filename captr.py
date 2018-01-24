#!/usr/local/bin/python3

import cv2
from time import sleep,time
cap = cv2.VideoCapture(0)
sleep(0.6)
ret,frame = cap.read()
rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
prefix = '~/'
out = cv2.imwrite(prefix+str(time())+'fak.jpg',frame)
cap.release()
