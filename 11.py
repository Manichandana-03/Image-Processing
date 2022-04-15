#11 RECTANGE /SQUARE

import cv2
import numpy as np
img=np.zeros((1000,1000,3)) #black background
#           image,start pt,   end pt,  color,   thickness
cv2.rectangle(img,(200,200),(700,700),(0,0,255),5)
cv2.imshow('RECTANGLE/SQUARE',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
    
