# 12.LIVE VIDEO FROM WEBCAM

import cv2

cap= cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    cv2.imshow('MY LIVE SKETCH',frame)
    if cv2.waitKey(1) == 13:
        break

cap.release()
cap.destroyAllWindows()
