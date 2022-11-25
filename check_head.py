import cv2
import numpy as np

img_rgb = cv2.imread('pictures/8.bmp')
img = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template1 = cv2.imread('img/comp1.bmp',0)
template2 = cv2.imread('img/temp1.png',0)
template3 = cv2.imread('img/temp2.png',0)

w1, h1 = template1.shape[::-1]
w2, h2 = template2.shape[::-1]
w3, h3 = template3.shape[::-1]

res1 = cv2.matchTemplate(img,template1,cv2.TM_CCOEFF_NORMED)
res2 = cv2.matchTemplate(img,template2,cv2.TM_CCOEFF_NORMED)
res3 = cv2.matchTemplate(img,template3,cv2.TM_CCOEFF_NORMED)

threshold1 = 0.87 #0.87
threshold2 = 0.95 #0.95
threshold3 = 0.80 #0.80

loc1 = np.where( res1 >= threshold1)
loc2 = np.where( res2 >= threshold2)
loc3 = np.where( res3 >= threshold3)

ptx1 = []
pty1 = []
ptr1 = []

ptx2 = []
pty2 = []
ptr2 = []

ptx3 = []
pty3 = []
ptr3 = []

print(len(loc1[0]))

for pt in zip(*loc1[::-1]):
    ptx1.append(pt[0])
    pty1.append(pt[1])
    
    cr = [x for x in ptr1 if abs(x[0]-pt[0]) < 50 and abs(x[1]-pt[1]) < 50]
    if cr:
        cr = cr[0]
        ptr1[ptr1.index(cr)] = ((cr[0] + pt[0])/2, (cr[1] + pt[1])/2)
    else:
        ptr1.append((pt[0], pt[1]))
cv2.rectangle(img_rgb, pt ,(pt[0]+ w1, pt[1]+ h1), (0,0,255), 2)
res_count1 = len(ptr1)           # get quantity of component


print(len(loc2[0]))

for pt in zip(*loc2[::-1]):
    ptx2.append(pt[0])
    pty2.append(pt[1])
    
    cr = [x for x in ptr2 if abs(x[0]-pt[0]) < 50 and abs(x[1]-pt[1]) < 50]
    if cr:
        cr = cr[0]
        ptr2[ptr2.index(cr)] = ((cr[0] + pt[0])/2, (cr[1] + pt[1])/2)
    else:
        ptr2.append((pt[0], pt[1]))
cv2.rectangle(img_rgb, pt, (pt[0] + w2, pt[1] + h2), (0,0,255), 2)
res_count2 = len(ptr2)           # get quantity of component


print(len(loc3[0]))

for pt in zip(*loc3[::-1]):
    ptx3.append(pt[0])
    pty3.append(pt[1])
    
    cr = [x for x in ptr3 if abs(x[0]-pt[0]) < 50 and abs(x[1]-pt[1]) < 50]
    if cr:
        cr = cr[0]
        ptr3[ptr3.index(cr)] = ((cr[0] + pt[0])/2, (cr[1] + pt[1])/2)
    else:
        ptr3.append((pt[0], pt[1]))
cv2.rectangle(img_rgb, pt, (pt[0] + w3, pt[1] + h3), (0,0,255), 2)
res_count3 = len(ptr3)           # get quantity of component



scale_percent = 50 # percent of original size
width = int(img_rgb.shape[1] * scale_percent / 100)
height = int(img_rgb.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
img_rgb = cv2.resize(img_rgb, dim, interpolation = cv2.INTER_AREA)

font = cv2.FONT_HERSHEY_SIMPLEX


if len(loc1[0]) > 0:    # Show text comp 1
    cv2.putText(img_rgb,'Comp1 OK '+ str(res_count1),(100,100), font, 1,(0,255,0),3,cv2.LINE_AA)
else:
    cv2.putText(img_rgb,'Comp1 NG ' + str(res_count1),(100,100), font, 1,(0,0,255),3,cv2.LINE_AA)

if len(loc2[0]) > 0:    # Show text comp 2
    cv2.putText(img_rgb,'Comp2 OK ' + str(res_count2),(100,200), font, 1,(0,255,0),3,cv2.LINE_AA)
else:
    cv2.putText(img_rgb,'Comp2 NG ' + str(res_count2),(100,200), font, 1,(0,0,255),3,cv2.LINE_AA)

if len(loc3[0]) > 0:    # Show text comp 3
    cv2.putText(img_rgb,'Comp3 OK ' + str(res_count3),(100,300), font, 1,(0,255,0),3,cv2.LINE_AA)
else:
    cv2.putText(img_rgb,'Comp3 NG ' + str(res_count3),(100,300), font, 1,(0,0,255),3,cv2.LINE_AA)


#cv2.imshow('template1', template1) #Show themplate
#cv2.imshow('template2', template2) #Show themplate
#cv2.imshow('template3', template3) #Show themplate

cv2.imshow('show', img_rgb)

#cv2.imshow('img', img)

cv2.waitKey(0)