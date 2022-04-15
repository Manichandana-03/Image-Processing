#Grayscale - black and white
import cv2
img=cv2.imread('images.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('ORIGINAL IMAGE',img)
cv2.imshow('GRAYSCALE IMAGE',gray)
cv2.waitKey(5000)
cv2.destroyAllWindows()
