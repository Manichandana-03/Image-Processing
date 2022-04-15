# LIVE CANNY SKETCH/VIDEO - EDGE DETECTION
import cv2

cap=cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    canny= cv2.Canny(frame,100,150)
    #100,150 are threshold values for best video
    #best edge detection
    #threshold values can be any(0 to 255)
    cv2.imshow("MY CANNY SKETCH",canny)
    if cv2.waitKey(1)==13:
        break

cap.release()
cv2.destroyAllWindows()
