import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, frame = cap.read()
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img_hsv = frame

    template = cv2.imread('pictures/.jpg', 0)
    w1, h1 = template.shape[::-1]

    template2 = cv2.imread('pictures/.jpg', 0)
    w2, h2 = template2.shape[::-1]

    template3 = cv2.imread('pictures/.jpg', 0)
    w3, h3 = template3.shape[::-1]

    template4 = cv2.imread('pictures/.jpg', 0)
    w4, h4 = template4.shape[::-1]

    template5 = cv2.imread('pictures/.jpg', 0)
    w5, h5 = template5.shape[::-1]

    template6 = cv2.imread('pictures/.jpg', 0)
    w6, h6 = template6.shape[::-1]

    template7 = cv2.imread('pictures/.jpg', 0)
    w7, h7 = template7.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    res2 = cv2.matchTemplate(img_gray, template2, cv2.TM_CCOEFF_NORMED)
    res3 = cv2.matchTemplate(img_gray, template3, cv2.TM_CCOEFF_NORMED)
    res4 = cv2.matchTemplate(img_gray, template4, cv2.TM_CCOEFF_NORMED)
    res5 = cv2.matchTemplate(img_gray, template5, cv2.TM_CCOEFF_NORMED)
    res6 = cv2.matchTemplate(img_gray, template6, cv2.TM_CCOEFF_NORMED)
    res7 = cv2.matchTemplate(img_gray, template7, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        img_hsv = cv2.rectangle(frame, pt, (pt[0]+w1, pt[1]+h1), (0, 0, 255), 2)
    
    threshold = 0.8
    loc = np.where(res2 >= threshold)
    for pt in zip(*loc[::-1]):
        img_hsv = cv2.rectangle(frame, pt, (pt[0]+w2, pt[1]+h2), (0, 255, 0), 2)
    
    threshold = 0.8
    loc = np.where(res3 >= threshold)
    for pt in zip(*loc[::-1]):
        img_hsv = cv2.rectangle(frame, pt, (pt[0]+w3, pt[1]+h3), (0, 0, 255), 2)

    threshold = 0.8
    loc = np.where(res4 >= threshold)
    for pt in zip(*loc[::-1]):
        img_hsv = cv2.rectangle(frame, pt, (pt[0]+w4, pt[1]+h4), (0, 255, 0), 2)

    threshold = 0.8
    loc = np.where(res5 >= threshold)
    for pt in zip(*loc[::-1]):
        img_hsv = cv2.rectangle(frame, pt, (pt[0]+w5, pt[1]+h5), (0, 0, 255), 2)

    threshold = 0.8
    loc = np.where(res6 >= threshold)
    for pt in zip(*loc[::-1]):
        img_hsv = cv2.rectangle(frame, pt, (pt[0]+w6, pt[1]+h6), (0, 255, 0), 2)

    threshold = 0.8
    loc = np.where(res7 >= threshold)
    for pt in zip(*loc[::-1]):
        img_hsv = cv2.rectangle(frame, pt, (pt[0]+w7, pt[1]+h7), (0, 0, 255), 2)

cv2.imshow('frame', img_hsv)
if cv2.waitKey(1) & 0xFF == ord('q'):
    break
else:
    break

cap.release()
cv2.destroyAllWindows()
