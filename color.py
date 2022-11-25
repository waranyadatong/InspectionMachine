import numpy as np
import cv2

img_rgb = cv2.imread('img/crack1.bmp')

scale_percent = 50 # percent of original size
width = int(img_rgb.shape[1] * scale_percent / 100)
height = int(img_rgb.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
img_rgb = cv2.resize(img_rgb, dim, interpolation = cv2.INTER_AREA)

    # Convert BGR to HSV
hsv = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_orange = np.array([17,120,200])
upper_orange = np.array([25,255,255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_orange, upper_orange)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(img_rgb,img_rgb, mask= mask)

cv2.imshow('img_rgb',img_rgb)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.waitKey(0)

cv2.destroyAllWindows()