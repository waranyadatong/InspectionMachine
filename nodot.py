from skimage.metrics import structural_similarity
import cv2
import numpy as np
import argparse
import imutils
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load input image
image = cv2.imread('pictures/dot.png')
modified = image.copy()

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_black = np.array([0,0,0], dtype = "uint8")
upper_black = np.array([50,50,50], dtype = "uint8")
mask = cv2.inRange(hsv, lower_black, upper_black)

# Find contours
cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Extract contours depending on OpenCV version
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

# Iterate through contours and filter by the number of vertices
for c in cnts:
    perimeter = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.04 * perimeter, True)
    if len(approx) > 2:
        cv2.drawContours(modified, [c], -1, (36, 255, 12), -1) #(36, 255, 12)

#cv2.imshow('Detected Image', mask)
cv2.imshow('Image-1', image)
cv2.imshow('Image-2', modified)
#cv2.imwrite('mask.png', mask)
cv2.imwrite('original.png', modified)
cv2.waitKey(0)
cv2.destroyAllWindows()






