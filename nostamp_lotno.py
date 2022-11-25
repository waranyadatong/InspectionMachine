import cv2
import numpy as np

# Read input image
image_lotno = cv2.imread('pictures/lotno.jpg')
original_lotno = image_lotno.copy()

# Convert it to grayscale
image_gray_lotno = cv2.cvtColor(image_lotno, cv2.COLOR_BGR2GRAY)

# Read template image
template = cv2.imread('pictures/lotno-temp.jpg',0)

# Store width and height of template in w and h
w, h = template.shape[::-1]

# Apply template matching
res = cv2.matchTemplate(image_gray_lotno, template, cv2.TM_CCOEFF_NORMED)

# Specify a threshold
threshold = 0.99

# Store the coordinates of matched area in a numpy array
loc = np.where(res >= threshold)

# Draw the rectangle around the mathed region
for pt in zip(*loc[::-1]):
    cv2.rectangle(image_lotno, pt, (pt[0] + w, pt[1] + h), (255, 0, 0), 2)

# Display result image eith the matched area
cv2.imshow('Original Image', original_lotno)
cv2.imshow('Result Image', image_lotno)
cv2.waitKey(0)
cv2.destroyAllWindows()

