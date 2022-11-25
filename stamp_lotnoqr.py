from skimage.metrics import structural_similarity
import cv2
import numpy as np
import argparse
import imutils
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load two input image
image_mix = cv2.imread('pictures/lotno.jpg')
image_md = cv2.imread('pictures/temp-3.jpg') #temp-3.jpg

# Resize for faster processing
resized_mix = cv2.resize(image_mix, (200, 150))
resized_md = cv2.resize(image_md, (200, 150))

# Convert image to grayscale
gray_mix = cv2.cvtColor(resized_mix, cv2.COLOR_BGR2GRAY)
gray_md = cv2.cvtColor(resized_md, cv2.COLOR_BGR2GRAY)

# Compute structural similarity index between images and obtain diferrences image
(score, diff) = structural_similarity(gray_mix, gray_md, full = True)
diff = (diff * 255).astype("uint8")
print("Structural Similarity Index: ", score)
if score < 1:
    x, y, w, h = 0, 0, 65, 195
    #cv2.rectangle(resized_mix, (x, x), (x + w, y + h), (0, 0, 0), -1)
    cv2.putText(resized_mix, "GOOD", (x + int(w/18), y + int(h/1.5)), cv2.FONT_HERSHEY_DUPLEX, 0.65, (255, 0, 0), 2)
    print("GOOD")
else:
    x, y, w, h = 0, 0, 65, 195
    #cv2.rectangle(resized_mix, (x, x), (x + w, y + h), (0, 0, 0), -1)
    cv2.putText(resized_mix, "NG", (x + int(w/18), y + int(h/1.5)), cv2.FONT_HERSHEY_DUPLEX, 0.59, (0, 0, 255), 2)
    #cv2.putText(resized_mix, "No Stamp QR Code", (5, 25),cv2.FONT_HERSHEY_DUPLEX, 0.59, (0, 0, 255), 2)
    print("NG")

# Obtain image contours
thresh = cv2.threshold(diff, 0 ,255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

# Plot image differences
for c in contours:
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(resized_mix, (x, y), (x + w, y + h), (0, 0, 255),2)
    cv2.rectangle(resized_md, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow("Original", resized_mix)
cv2.imshow("Modified", resized_md)
#cv2.imshow("Thresh", thresh)
#cv2.imshow("Diff", diff)
cv2.waitKey(0)
cv2.destroyAllWindows()

