import cv2
import numpy as np

img_rgb = cv2.imread('img/crack2.bmp')
img = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('img/template.bmp',0)

print(template.shape[::-1])

w, h = template.shape[::-1]