import cv2
import numpy as np

img_rgb = cv2.imread('img/color.bmp')
img = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('img/template.bmp',0)

w, h = template.shape[::-1]

res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)

threshold = 0.8

loc = np.where( res >= threshold)

# print(loc)

pt0 = [a[0] for a in zip(*loc[::-1])]
pt1 = [a[1] for a in zip(*loc[::-1])]
crop_img = np.zeros(shape=[512, 512, 3], dtype=np.uint8)
crop_img_bw = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

if len(pt0) > 0:
    pt = (int(sum(pt0)/len(pt0)), int(sum(pt1)/len(pt1)))

    print(pt)

    crop_img = img_rgb[pt[1]:pt[1]+h, pt[0]:pt[0]+w].copy()

    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

scale_percent = 50 # percent of original size
width = int(img_rgb.shape[1] * scale_percent / 100)
height = int(img_rgb.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
img_rgb = cv2.resize(img_rgb, dim, interpolation = cv2.INTER_AREA)

cv2.imshow('crop', crop_img)

cv2.imshow('show', img_rgb)

cv2.imshow('template', template)

cv2.waitKey(0)
