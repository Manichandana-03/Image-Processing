#shortcut to convert image to grayscale
import cv2
img=cv2.imread('images.jpg',0)
cv2.imshow('GRAYSCALE IMAGE',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
    
