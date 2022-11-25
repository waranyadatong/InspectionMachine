from skimage.metrics import structural_similarity
import cv2
import numpy as np
import argparse
import imutils
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load input image
image_1 = cv2.imread('pictures/.jpg')
image_2 = cv2.imread('pictures/.jpg')

# Copy image
imagecop = image_1.copy()

# Resize for faster processing
resize_1 = cv2.resize(image_1, (200, 150)) # w*h 
resize_2 = cv2.resize(image_2, (200, 150)) # w*h

# Convert image to grayscale
grayimg_1 = cv2.cvtColor(resize_1, cv2.COLOR_BGR2GRAY)
grayimg_2 = cv2.cvtColor(resize_2, cv2.COLOR_BGR2GRAY)

# Compute SSIM between two images
(score, diff) = structural_similarity(grayimg_1, grayimg_2, full = True)
diff = (diff * 255).astype("uint8")
print("Similarity Score: {:.3f}%".format(score * 100))

# Obtain image contours
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

# Plot images differences
for cnt in contours:
    (x, y, w, h) = cv2.boundingRect(cnt)
    cv2.rectangle(resize_1, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.rectangle(resize_2, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow("Img-1", resize_1)
cv2.imshow("Img-2", resize_2)
cv2.imshow("Img-Thresh", thresh)
cv2.imshow("Img-Diff", diff)
cv2.waitKey(0)
cv2.destroyAllWindows()
