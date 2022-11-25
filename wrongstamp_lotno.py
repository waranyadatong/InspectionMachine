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

# Convert image to grayscale
img_cop = image_1.copy()

# Resize for faster processing
res_1 = cv2.resize(image_1, (200, 150)) # w*h
res_2 = cv2.resize(image_2, (200, 150)) # w*h

# Convert image to grayscale
grayim_1 = cv2.cvtColor(res_1, cv2.COLOR_BGR2GRAY)
grayim_2 = cv2.cvtColor(res_2, cv2.COLOR_BGR2GRAY)

# Compute SSIM between two images
(score, diff) = structural_similarity(grayim_1, grayim_2, full = True)
diff = (diff * 255).astype("uint8")
print("Similarity Score: ", score)

# Obtain image contours
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

# Plot images differences
for cnt in contours:
    (x, y, w, h) = cv2.boundingRect(cnt)
    cv2.rectangle(res_1, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.rectangle(res_2, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow("Image-1", res_1)
cv2.imshow("Image-2", res_2)
cv2.imshow("Image-Thresh", thresh)
cv2.imshow("Image-Diff", diff)
cv2.waitKey(0)
cv2.destroyAllWindows()