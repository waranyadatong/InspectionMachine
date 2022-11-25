import cv2
import numpy as np

image = cv2.imread('pictures/markdot.png')
image = cv2.medianBlur(image, 5)
cimg = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
circles = CV2.HoughCircles(image, cv2.HOUGH_GRADIENT,1,10,param1 = 100, param2 = 30, minRadius = 1, maxRadius = 15)

circles = np.uint16(np.around(circles))
counter = 0

for i in circles[0,:]:
    cv2.circle(cimg,(i[0],i[1],i[2],(0,255,0),3))
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    counter += 1
strin = 'Mark Dot : ' + str(counter-1)
cv2.rectangle(cimg, (0, 0), (190, 45), (0,0,0), -1)
cv2.putText(cimg, strin,(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1,cv2.LINE_AA)
cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()