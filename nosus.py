import cv2
import numpy as np

# Read input image
image_sus = cv2.imread('pictures/sus.jpg')
original_sus = image_sus.copy()

# Convert it to grayscale
image_gray_sus = cv2.cvtColor(image_sus, cv2.COLOR_BGR2GRAY)

# Read template image
template = cv2.imread('pictures/sus-temp.jpg', 0)

# Store width and height of template in w and h
w, h = template.shape[::-1]

# Apply template matching
res = cv2.matchTemplate(image_gray_sus, template, cv2.TM_CCOEFF_NORMED)

# Specify a threshold
threshold = 0.8

# Store the coordinates of matched area in a numpy array
loc = np.where(res >= threshold)

# Draw the rectangle around the matched region
for pt in zip(*loc[::-1]):
    cv2.rectangle(image_sus, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

# Display result image eith the matched area
cv2.imshow('Original Image', original_sus)
cv2.imshow('Result Image', image_sus)
cv2.waitKey(0)
cv2.destroyAllWindows()
