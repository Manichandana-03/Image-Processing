import cv2
img=cv2.imread('images.jpg',0)# 0  converts into grayscale
cv2.imshow('GRAY SCALE IMAGE',img)
cv2.waitKey(3000)
#==============threshold(img source,min val,max val,type of conversion)
ret,binary =cv2.threshold(img,124,255,cv2.THRESH_BINARY)
 #ret is the dummy variable which we don not use
# but we must have to take ret variables, i.e.,we should have to refer 2 variables


cv2.imshow('BINARY IMAGE',binary)
cv2.waitKey(0)
cv2.destroyAllWindows()

