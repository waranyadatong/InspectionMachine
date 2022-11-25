import cv2
import numpy as np

# Read input image
image_folding = cv2.imread('pictures/folding.jpg')
original_folding = image_folding.copy()

# Convert it to grayscale
image_gray_folding = cv2.cvtColor(image_folding, cv2.COLOR_BGR2GRAY)

# Read template image
template = cv2.imread('pictures/folding-temp.jpg', 0)

# Store width and height of template in w and h
w, h = template.shape[::-1]

# Apply template matching
res = cv2.matchTemplate(image_gray_folding, template, cv2.TM_CCOEFF_NORMED)

# Specify a threshold
threshold = 0.8

# Store the coordinates of matched area in a numpy array
loc = np.where(res >= threshold)

# Draw the rectangle around the matched region
for pt in zip(*loc[::-1]):
    cv2.rectangle(image_folding, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

# Display result image eith the matched area
cv2.imshow('Original Image', original_folding)
cv2.imshow('Result Image', image_folding)
cv2.waitKey(0)
cv2.destroyAllWindows()
