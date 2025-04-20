import cv2

cat = cv2.imread("cat.png")
cat2 = cv2.imread("cat2.png", cv2.IMREAD_GRAYSCALE)
cat1 = cv2.cvtColor(cat, cv2.COLOR_BGR2GRAY)

diff = cv2.absdiff(cat1, cat2)

thresh = cv2.threshold(diff,25,255,cv2.THRESH_BINARY)[1]
thresh = cv2.dilate(thresh,None,iterations=2)

contours,hierrachy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,
                                      cv2.CHAIN_APPROX_SIMPLE)

for  contour in contours:
    x,y,w,h = cv2.boundingRect(contour)
    cv2.rectangle(cat,(x,y),(x+w,y+h),(0,255,0),2)

cv2.putText(cat,f"Differences = {len(contours)}",(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,0))
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.imshow("Original", cat)
cv2.namedWindow("Differences", cv2.WINDOW_NORMAL)
cv2.imshow("Differences", thresh)
cv2.waitKey()