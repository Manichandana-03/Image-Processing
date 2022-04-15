# 14.FACE RECOGNITION
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('abc.jpg') #reading abc.jpg
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converts into gray scale

faces =  face_cascade.detectMultiScale(gray,1.1,9)
# 1.1 is scaleFactor,minNeighbors =9


for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
    #x,y -  starting pt,(x+w,y+h)-end pt,(0,255,0)-green color,5 -thickness


cv2.imshow('FACE RECOGNITION',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
