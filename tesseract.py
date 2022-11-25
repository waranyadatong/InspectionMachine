import numpy as np 
import cv2

# load image
image = cv2.imread('pictures/pytes.jpg') # pictures/pytes.jpg // pictures/lot-2.png

# create grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# perform threshold
retr, mask = cv2.threshold(gray_image, 190, 255, cv2.THRESH_BINARY)

# findcontours
#ret, contours, hier = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# select the largest contour
largest_area = 0
for cnt in contours:
    if cv2.contourArea(cnt) > largest_area:
        cont = cnt
        largest_area = cv2.contourArea(cnt)

# find the rectangle (and the cornerpoints of that rectangle) that surrounds the contours / photo
rect = cv2.minAreaRect(cont)
box = cv2.boxPoints(rect)
box = np.int0(box)

# Warp image to square
# assign cornerpoints of the region of interest
pts1 = np.float32([box[2],box[3],box[1],box[0]])
# provide new coordinates of cornerpoints
pts2 = np.float32([[0,0],[500,0],[0,110],[500,110]])

# determine and apply transformationmatrix
M = cv2.getPerspectiveTransform(pts1,pts2)
tmp = cv2.warpPerspective(image,M,(500,110))

# create grayscale
gray_image2 = cv2.cvtColor(tmp, cv2.COLOR_BGR2GRAY)
# perform threshold
retr, mask2 = cv2.threshold(gray_image2, 160, 255, cv2.THRESH_BINARY_INV)

# remove noise / close gaps
kernel =  np.ones((5,5),np.uint8)
result = cv2.morphologyEx(mask2, cv2.MORPH_CLOSE, kernel)

# draw rectangle on original image
cv2.drawContours(image, [box], 0, (255,0,0), 2)

# dilate result to make characters more solid
kernel2 =  np.ones((3,3),np.uint8)
result = cv2.dilate(result,kernel2,iterations = 1)

# invert to get black text on white background
result = cv2.bitwise_not(result)

# show image
cv2.imshow("Result", result)
cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()