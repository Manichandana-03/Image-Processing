import cv2
import numpy as np
img=np.zeros((500,500,3))
img[:] = 2,0,255
cv2.imshow('COLOR BACKGROUND',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
