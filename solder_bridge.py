import numpy as np
import cv2

img_rgb = cv2.imread('pictures/8.bmp')

scale_percent = 50 # percent of original size
width = int(img_rgb.shape[1] * scale_percent / 100)
height = int(img_rgb.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
img_rgb = cv2.resize(img_rgb, dim, interpolation = cv2.INTER_AREA)

# Convert BGR to HSV
hsv = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_metal = np.array([15,0,100])
upper_metal = np.array([40,76,150])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_metal, upper_metal)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(img_rgb,img_rgb, mask= mask)

cnts, hierarchy = cv2.findContours(mask, 1, 2)

# cnt_list = [cv2.contourArea(cnt) for cnt in cnts]

cnt_list = []
for cnt in cnts:
    area = cv2.contourArea(cnt)
    cnt_list.append((area, cnt))

# print(sorted(cnt_list))

if all(cnt_tuple[0] < 5000 for cnt_tuple in cnt_list):
    print('No Solder Bridge')
else:
    print('Solder Bridge Found')
    for cnt_tuple in cnt_list:
        if cnt_tuple[0] >= 5000:
            x,y,w,h = cv2.boundingRect(cnt_tuple[1])
            img_rgb = cv2.rectangle(img_rgb,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow('img_rgb',img_rgb)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.waitKey(0)

cv2.destroyAllWindows()