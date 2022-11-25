import cv2
import numpy as np

image = cv2.imread("pictures/lot-1.png")
thresh = cv2.threshold(image, 115, 255, cv2.THRESH_BINARY_INV)[1]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3)) #
dilate = cv2.dilate(thresh, kernel, iterations=1)
final = cv2.threshold(dilate, 115, 255, cv2.THRESH_BINARY_INV)[1]

#Show the image, note that the name of the output window must be same
cv2.imshow('image', image)
cv2.imshow('dilate', dilate)
cv2.imshow('final', final)

#To load and hold the image
cv2.waitKey(0)

#To close the window after the required kill value was provided
cv2.destroyAllWindows()






