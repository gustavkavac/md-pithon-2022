#!/usr/bin/env python3
'''
Python 6 nodarbības mājasdarbs Nr.3

Uzdevums: aizpildīt vietas ar atzīmi TODO
'''

import numpy as np
import cv2

# importēt "python.jpg" bildi

img = cv2.imread('python.jpg')
cv2.imshow('img', img)

# Pārveidot bildi melnbaltu un izvadīt uz ekrāna
img_peleks = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) # TODO
(thresh, img_melnbalts) = cv2.threshold(img_peleks, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Melnbalta bilde', img_melnbalts)

# pielietot Caddy edge detection uz originālās bildes un izvadīt uz ekrāna
img_caddy = cv2.Canny(image=img, threshold1=100, threshold2=200) # TODO

cv2.imshow('Canny', img_caddy)

# Pārveidot TIKAI zilo krāsu par sarkanu un izvadīt uz ekrāna


sensitivity = 5
gain = 120

def changer(image, sensitivity, strength):
    for row in image:
        for pixel in row:
            b = pixel[0]
            g = pixel[1]
            r = pixel[2]
            if (b > g + sensitivity) & (b > r + sensitivity):
                if pixel[2] + strength > 255:
                    pixel[2] = 255
                    pixel[0] = 0
                else:
                    pixel[2] = r + strength
                    pixel[0] = 0
    return image
                
ra_img = changer(img, sensitivity, gain)

cv2.imshow('ra_img', ra_img)

cv2.waitKey()
cv2.destroyAllWindows()