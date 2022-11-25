import cv2
import numpy as np

img_rgb = cv2.imread('pictures/8.bmp')
img = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('img/comp1.bmp',0)

w, h = template.shape[::-1]

res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)

threshold = 0.9

loc = np.where( res >= threshold)

ptx1 = []
pty1 = []
ptr1 = []

# get location of template matching result
for pt in zip(*loc[::-1]):
    ptx1.append(pt[0])
    pty1.append(pt[1])
    cr = [x for x in ptr1 if abs(x[0]-pt[0]) < 50 and abs(x[1]-pt[1]) < 50]
    if cr:
        cr = cr[0]
        ptr1[ptr1.index(cr)] = ((cr[0] + pt[0])/2, (cr[1] + pt[1])/2)
    else:
        ptr1.append((pt[0], pt[1]))

res_count1 = len(ptr1)           # get quantity of component

x_box = 724
y_box = 100
w_box = 86  #--->
h_box = 548 # V

# get border contour
find_line_img = img[y_box:y_box+h_box, x_box:x_box+w_box]
cv2.imwrite('line.bmp', find_line_img)
find_line_img = cv2.GaussianBlur(find_line_img,(11,11),0)
th = cv2.adaptiveThreshold(find_line_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,21,5)
kernel = np.ones((3,3),np.uint8)
cv2.imshow('thth', th)
th = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
cv2.imshow('close', th)
th = cv2.bitwise_not(th)
kernel = np.ones((21,21),np.uint8)
th = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
th = cv2.bitwise_not(th)
cv2.imshow('th', th)
#_, contours, hierarchy = cv2.findContours(th, 1, 2)
contours, hierarchy = cv2.findContours(th, 1, 2)

max_area = 0                                       
max_cnt = contours[0]
for cnt in contours:
    if cv2.contourArea(cnt) > max_area:
        max_cnt = cnt
        max_area = cv2.contourArea(cnt)
x_cnt,y_cnt,w_cnt,h_cnt = cv2.boundingRect(max_cnt)                 # region of interest

# draw border line
cv2.line(img_rgb,(x_box + w_cnt, y_box),(x_box + w_cnt, y_box + h_cnt),(0,255,0),2)

cv2.imshow('find_line_img', find_line_img)

# get list of border x, y
cnt_list = []
for cnt in max_cnt:
    [[x, y]] = cnt
    cnt_list.append([x,y])
cnt_list = sorted(cnt_list, key=lambda a: a[1])
print(cnt_list)

# loop through each template matching result
for pt in ptr1:
    flag = True
    # draw template matching result
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    # draw line from border to center of template matching result
    y_center_of_matching = int(pt[1]+h/2)
    x_center_of_matching = int(pt[0]+w/2)
    cv2.line(img_rgb,(x_box+w_cnt, y_center_of_matching),(x_center_of_matching, y_center_of_matching),(255,0,0),2)

    for cnt in cnt_list:
        # check if y(center of matching) = y(border line)
        if cnt[1] + y_box >= y_center_of_matching and flag:
            length = abs((cnt[0]+x_box)-x_center_of_matching)
            font = cv2.FONT_HERSHEY_SIMPLEX
            # assign manually
            x_threshold = 875

            if x_center_of_matching > x_threshold - w/2 and x_center_of_matching < x_threshold + w/2 :
                cv2.putText(img_rgb,'{} px OK'.format(length),(cnt[0]+x_box, int(pt[1]+h/2)), font, 2,(0,255,0),3,cv2.LINE_AA)
            else:
                cv2.putText(img_rgb,'{} px NG'.format(length),(cnt[0]+x_box, int(pt[1]+h/2)), font, 2,(0,0,255),3,cv2.LINE_AA)

            flag = False



scale_percent = 50 # percent of original size
width = int(img_rgb.shape[1] * scale_percent / 100)
height = int(img_rgb.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
img_rgb = cv2.resize(img_rgb, dim, interpolation = cv2.INTER_AREA)

cv2.imshow('show', img_rgb)

cv2.imshow('template', template)

cv2.waitKey(0)
