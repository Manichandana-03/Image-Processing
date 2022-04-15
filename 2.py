import cv2
img=cv2.imread('images.jpg')
cv2.imshow('ORIGINAL IMAGE',img)
cv2.imwrite('lenovo.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
