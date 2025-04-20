import cv2
import time 
cv2.namedWindow("Camera",cv2.WINDOW_NORMAL)
cv2.namedWindow("Background" ,cv2.WINDOW_NORMAL)

capture = cv2.VideoCapture(0)

capture.set(cv2.CAP_PROP_AUTO_EXPOSURE,3)
capture.set(cv2.CAP_PROP_AUTO_EXPOSURE,1)
capture.set(cv2.CAP_PROP_EXPOSURE,9030)


min_area = 1000
background = None

while capture.isOpened( ):
    ret,frame = capture.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)
    key = chr(cv2.waitKey(1)& 0xFF)
    if key == "q":
        break
    if key =="b":
        background = gray.copy()
    if background is not None:
        delta = cv2.absdiff(background,gray)
        thresh = cv2.threshold(delta,100,255,cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh,None,iterations=2)
        cv2.imshow("Background", thresh)
        contors,_=cv2.findContours(thresh,cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)
        for contour in contors:
            area = cv2.contourArea(contour)
            if area>min_area:
                x,y,w,h = cv2.boundingRect(contour)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("Camera",frame)

capture.release()
cv2.destroyAllWindows()
