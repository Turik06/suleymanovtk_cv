import cv2
import numpy as np

image = cv2.imread("rose.jpg")

hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

lower = np.array([0,200,100])
upper = np.array([1,255,255])

mask = cv2.inRange(hsv,lower,upper)
# mask = cv2.dilate(mask,np.ones((7,7)))
mask = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,np.ones((11,11)),iterations=2)
rose = cv2.bitwise_and(image,image,mask=mask)



cv2.imshow("Image",image)
cv2.imshow("Mask",mask)
cv2.imshow("Rose",rose)
cv2.waitKey()
cv2.destroyAllWindows()