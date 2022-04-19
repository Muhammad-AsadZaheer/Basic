# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 08:50:50 2022

@author: Asad
"""

#import related libraries

import cv2
from skimage.filters import sobel 

#reading image from the directory

read_img= cv2.imread("index.jpg")


#Sobel is an edge detection filter

edge_sobel = sobel(read_img)

#showing the normal image which we used

cv2.imshow("img", read_img)

#showing the Sobel filtered image

cv2.imshow("edge", edge_sobel)


#printing the shapes of bothe normal and sobel image

print(read_img.shape)
print(edge_sobel.shape)

#To close the window

cv2.waitKey()
cv2.destroyAllWindows()