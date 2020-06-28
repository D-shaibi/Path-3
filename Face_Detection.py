import cv2
import numpy

# downloaded the file from github
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

videocapture = cv2.VideoCapture(0)

while True:
    ret, pic = videocapture.read()
    faces= face_cascade.detectMultiScale(pic, 1.5, 4)
    for (x, y, w, h) in faces:
        cv2.circle(pic,(int(x+w/2),int(y+h/2)),int(h/2),(255,255,255),2)
        cv2.putText(pic,'person',(x,y), cv2.FONT_HERSHEY_TRIPLEX, 2, (255,255,255), 2)
    
    cv2.imshow('face_detection', pic)
    k= cv2.waitKey(30) & 0xff
    if k == ord('q'):
        break
    
cv2.destroyAllWindows()
