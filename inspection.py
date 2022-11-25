import cv2
import numpy as np

def template_matching():
    img_rgb = cv2.imread('img/crack2.bmp')
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
    upper_orange = np.array([25,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_orange, upper_orange)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img,img, mask= mask)

    return res, mask


if __name__ == "__main__":
    img = template_matching()

    res, mask = color_detect(img)

    cv2.imshow('crop', img)

    cv2.imshow('res', res)

    cv2.imshow('mask', mask)

    cv2.waitKey(0)