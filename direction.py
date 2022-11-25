import cv2
import numpy as np

img_rgb = cv2.imread('img/good.bmp')
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

    crop_img_bw = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

th = cv2.adaptiveThreshold(crop_img_bw,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,33,28)

cv2.imshow('threshold', th)


th = cv2.bitwise_not(th)

#_, contours, hierarchy = cv2.findContours(th, 1, 2)
contours, hierarchy = cv2.findContours(th, 1, 2)

if len(contours) > 0:
    max_area = 0 # optimized later
    less_max_area = 0
    max_cnt = contours[0]
    less_max_cnt = contours[0]

    for cnt in contours:
        if cv2.contourArea(cnt) > max_area:
            less_max_cnt = max_cnt
            less_max_area = max_area
            max_cnt = cnt
            max_area = cv2.contourArea(cnt)
        elif cv2.contourArea(cnt) > less_max_area:
            less_max_cnt = cnt
            less_max_area = cv2.contourArea(cnt)
    x_max,y_max,w_max,h_max = cv2.boundingRect(max_cnt)                 # region of interest
    x_less,y_less,w_less,h_less = cv2.boundingRect(less_max_cnt)                 # region of interest
    print(x_max,y_max,w_max,h_max)
    print(x_less,y_less,w_less,h_less)

    font = cv2.FONT_HERSHEY_SIMPLEX

    if y_less < h/2 and y_max < h/2:
        print("Marker is on the top")
        cv2.putText(img_rgb,"Marker is on the top",(430,200), font, 2,(0,255,0),3,cv2.LINE_AA)
    else:
        print("Marker is on the bottom")
        cv2.putText(img_rgb,'Marker is on the bottom',(100,100), font, 1,(0,255,0),3,cv2.LINE_AA)


img_w, img_h = crop_img_bw.shape[::-1]

scale_percent = 50 # percent of original size
width = int(img_rgb.shape[1] * scale_percent / 100)
height = int(img_rgb.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
img_rgb = cv2.resize(img_rgb, dim, interpolation = cv2.INTER_AREA)

cv2.imshow('img_rgb', img_rgb)


cv2.imshow('crop', crop_img_bw)

cv2.imshow('template', template)

# cv2.imshow('threshold', th)

# cv2.imshow('show', img_rgb)


cv2.waitKey(0)
