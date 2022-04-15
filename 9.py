#9 RGB EXTRACTION from image
#RED, GREEN AND BLUE TINT

import numpy as np
import cv2
img=cv2.imread('images.jpg')
cv2.imshow('ORGINAL IMAGE',img)

B,G,R = cv2.split(img)
#here we are taking 3 color channels and spliting them
#cv2.split() is used to split coloured/multi channel imgae into seperate single channel images
zeros = np.zeros(img.shape[:2],dtype = 'uint8')
# we are only considering len and width and ignoring channel
cv2.imshow('RED',cv2.merge([zeros,zeros,R]))
#cv2.merge() merges several single channel images into multichannel images
# it merges red plane with black background
cv2.imshow('GREEN',cv2.merge([zeros,G,zeros]))
cv2.imshow('BLUE',cv2.merge([B,zeros,zeros]))
cv2.waitKey(0)
cv2.destroyAllWindows()
