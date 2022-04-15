#10.EDGE DETECTION - SOBEL,GAPLACIAN ,CANNY -->(TYPES)
import cv2
img=cv2.imread('images.jpg',0)# 0 converts into grayscale

laplacian = cv2.Laplacian(img,cv2.CV_8U)
#CV_U8 - Unsigned 8 bit/pixel

cv2.imshow('Lapacian Image',laplacian) #converts img into laplacian edge detecting technique

canny = cv2.Canny(img,90,200)
cv2.imshow('Canny Image',canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
