import cv2
import pytesseract
import re
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = cv2.imread("pictures/lot-2.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 2)
erode = cv2.erode(thresh, np.array((7, 7)), iterations=1)
text = pytesseract.image_to_string(erode, config="--psm 6")
text = re.sub('[^A-Za-z0-9]+', '\n', text)
print(text)