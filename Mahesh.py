from tkinter import *

from PIL import Image, ImageTk

import matplotlib.pyplot as plt #plt is object

from tkinter import filedialog

import cv2

import matplotlib.pyplot as plt

import numpy as np

b=cv2.imread("tmp.jpg")

# changes here

# creating a hsv image and from that creating a binary image required for findContours

gray = cv2.cvtColor(b, cv2.COLOR_BGR2HSV)

lower = np.array([0, 48, 80], dtype="uint8")

upper = np.array([20, 255, 255], dtype="uint8")

binary = cv2.inRange(gray, lower, uupper

#a=cv2.cvtColor(b,0)

#kernel=np.ones([2,2], np.uint8) #???

#_, thresh= cv2.threshold(a, 245,255, cv2.THRESH_BINARY)

cv2.imshow("threshold", gray)

cv2.waitKey(0)

cv2.destroyAllWindows()

j,_ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

k=cv2.drawContours(b,j, -1, (255,255,255),2)

cv2.imshow("contours", k)

cv2.waitKey(0)  #changes here

cv2.destroyAllWindows()
