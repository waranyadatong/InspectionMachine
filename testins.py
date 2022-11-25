import numpy as np
import cv2

image = cv2.imread('pictures/sus-2.png')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([0, 5, 50]) # lower_orange = np.array([0, 22, 167])
upper = np.array([179, 50, 255]) # upper_orange = np.array([179, 255, 255])
mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow('result', result)
cv2.waitKey()
