import cv2
import numpy as np

def template_matching():
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

        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

    scale_percent = 50 # percent of original size
    width = int(img_rgb.shape[1] * scale_percent / 100)
    height = int(img_rgb.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    img_rgb = cv2.resize(img_rgb, dim, interpolation = cv2.INTER_AREA)

    return crop_img

def color_detect(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_orange = np.array([17,120,200])
    upper_orange = np.array([27,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_orange, upper_orange)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img,img, mask= mask)

    return res, mask

def get_contours(img, res):

    # img = cv2.imread('mask.jpg',0)
    ret,thresh = cv2.threshold(img,127,255,0)
    #_, contours, hierarchy = cv2.findContours(thresh, 1, 2)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)

    if len(contours) > 0:
        max_area = 0                                        # optimized later
        max_cnt = contours[0]
        for cnt in contours:
            if cv2.contourArea(cnt) > max_area:
                max_cnt = cnt
                max_area = cv2.contourArea(cnt)
        x,y,w,h = cv2.boundingRect(max_cnt)                 # region of interest
        print(x, y, w, h)               

        cv2.rectangle(res, (x, y), (x + w, y + h), (0,0,255), 2)

        mask_not = cv2.bitwise_not(mask)         # focus on black box

        kernel = np.ones((5,5),np.uint8)

        mask_not = cv2.morphologyEx(mask_not, cv2.MORPH_OPEN, kernel)

        cv2.imshow('mask_not', mask_not)

        #_, cnts, _ = cv2.findContours(mask_not, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts, _ = cv2.findContours(mask_not, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        cnt_box = []
        flag = True
        print(len(cnts))
        for cnt in cnts:    
            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            print(box)

            minx = min(i[0] for i in box)
            maxx = max(i[0] for i in box)
            miny = min(i[1] for i in box)
            maxy = max(i[1] for i in box)


            for i in box:
                cv2.rectangle(res, (minx, miny), (maxx, maxy), (0,0,255), 2)

                if not (i[1] >= y and i[1] <= y + h and i[0] >= x and i[0] <= x + w and flag):      # if contour is in the box, flag = true
                    flag = False
            
            if flag:
                cnt_box.append(box)
                cv2.rectangle(res, (minx, miny), (maxx, maxy), (0,255,0), 2)
                

            flag = True

        print(len(cnt_box))


if __name__ == "__main__":
    img = template_matching()

    res, mask = color_detect(img)

    M = get_contours(mask, res)



    cv2.imshow('crop', img)

    cv2.imshow('res', res)
    
    cv2.imshow('mask', mask)

    cv2.waitKey(0)