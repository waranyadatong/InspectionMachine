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
image_cop = image_1.copy()

# Resize for faster processing
resized_1 = cv2.resize(image_1, (200, 150)) # w*h
resized_2 = cv2.resize(image_2, (200, 150)) # w*h

# Convert image to grayscale
gray_1 = cv2.cvtColor(resized_1, cv2.COLOR_BGR2GRAY)
gray_2 = cv2.cvtColor(resized_2, cv2.COLOR_BGR2GRAY)

# Compute SSIM between two images
(score, diff) = structural_similarity(gray_1, gray_2, full = True)
print("Similarity Score: {:.3f}%".format(score * 100))
#print("Similarity Score: ", score)
diff = (diff * 255).astype("uint8")

# Obtain image contours
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
#contours = contours[0] if len(contours) == 2 else contours[1]

# Plot image differences 
for cnt in contours:
    (x, y, w, h) = cv2.boundingRect(cnt)
    cv2.rectangle(resized_1, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.rectangle(resized_2, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("Img Ori", resized_1)
cv2.imshow("Img Modi", resized_2)
cv2.imshow("Img Thres", thresh)
cv2.imshow("Img Diff", diff)
cv2.waitKey(0)
cv2.destroyAllWindows()