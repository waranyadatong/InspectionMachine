import cv2
import numpy as np
import argparse
import imutils
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.metrics import structural_similarity

image_lot = cv2.imread('pictures/dot.png')
image_mod = cv2.imread('pictures/nodot.png')

resize_lot = cv2.resize(image_lot, (200, 150))
resize_mod = cv2.resize(image_mod, (200, 150))

gray_lot = cv2.cvtColor(resize_lot, cv2.COLOR_BGR2GRAY)
gray_mod = cv2.cvtColor(resize_mod, cv2.COLOR_BGR2GRAY)

(score, diff) = structural_similarity(gray_lot, gray_mod, full = True)
diff = (diff * 255).astype("uint8")
print("Structural Similarity : ", score)
if score < 1:
    x, y, w, h = 0, 0, 185, 35
    cv2.rectangle(resize_lot, (x, x), (x + w, y + h), (0, 0, 0), -1)
    cv2.putText(resize_lot, "GOOD", (x + int(w/18), y + int(h/1.5)), cv2.FONT_HERSHEY_DUPLEX, 0.65, (255, 255, 255), 2)
    print("GOOD")
else:
    x, y, w, h = 0, 0, 195, 35
    cv2.rectangle(resize_lot, (x, x), (x + w, y + h), (0, 0, 0), -1)
    cv2.putText(resize_lot, "NG", (x + int(w/18), y + int(h/1.5)), cv2.FONT_HERSHEY_DUPLEX, 0.59, (0, 0, 255), 2)
    #cv2.putText(resized_qr, "No Stamp QR Code", (5, 25),cv2.FONT_HERSHEY_DUPLEX, 0.59, (0, 0, 255), 2)
    print("NG")

# Obtain image contours
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

# Plot image differences (loop over contours)
for c in contours:
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(resized_lot, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.rectangle(resized_mod, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow("Original", resized_lot)
cv2.imshow("Modified", resized_mod)
#cv2.imshow("Thresh", thresh)
#cv2.imshow("Diff", diff)
cv2.waitKey(0)
cv2.destroyAllWindows()
