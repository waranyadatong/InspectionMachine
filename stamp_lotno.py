from skimage.metrics import structural_similarity
import cv2
import numpy as np
import argparse
import imutils
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load two input image
image_lotno = cv2.imread('pictures/lotno.jpg') # lotno.jpg
image_mod = cv2.imread('pictures/lotno-temp-1.jpg')

# Resize for faster processing
resized_lotno = cv2.resize(image_lotno, (200, 150)) # w*h
resized_mod = cv2.resize(image_mod, (200, 150)) # w*h

# Convert image to grayscale
gray_lotno = cv2.cvtColor(resized_lotno, cv2.COLOR_BGR2GRAY)
gray_mod = cv2.cvtColor(resized_mod, cv2.COLOR_BGR2GRAY)

# Compute structural similarity index between images and obtain difference image
(score, diff) = structural_similarity(gray_lotno, gray_mod, full = True)
diff = (diff * 255).astype("uint8")
print("Structural Similarity Index: ", score)
if score < 1:
    x, y, w, h = 0, 0, 65, 195
    #cv2.rectangle(resized_lotno, (x, x), (x + w, y + h), (0, 0, 0), -1)
    cv2.putText(resized_lotno, "GOOD", (x + int(w/18), y + int(h/1.5)), cv2.FONT_HERSHEY_DUPLEX, 0.7, (36, 255, 12), 2)
    print("GOOD")
else:
    x, y, w, h = 0, 0, 35, 195
    #cv2.rectangle(resized_lotno, (x, x), (x + w, y + h), (0, 0, 0), -1)
    cv2.putText(resized_lotno, "NG", (x + int(w/18), y + int(h/1.5)), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 0, 255), 2)
    print("NG")

# Obtain image contours
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

# Plot image differences (loop over contours)
for c in contours:
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(resized_lotno, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.rectangle(resized_mod, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow("Original", resized_lotno)
cv2.imshow("Modified", resized_mod)
#cv2.imshow("Diff", diff)
#cv2.imshow("Thresh", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()


