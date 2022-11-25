import cv2
import numpy as np
from PIL import Image

orgImg = cv2.imread("ca.png")

image11 = cv2.cvtColor(orgImg, cv2.COLOR_BGR2GRAY)

cv2.normalize(image11, image11, 70, 255, cv2.NORM_MINMAX)
ret, black_mask = cv2.threshold(image11, 110, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("Original image", orgImg)
cv2.imshow("Final image", black_mask)
cv2.waitKey(0)

cv2.imwrite("ca_blackmask.png", black_mask)