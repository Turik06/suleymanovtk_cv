import cv2
import matplotlib.pyplot as plt

mushroom = cv2.imread("mushroom.jpg")
logo = cv2.imread("cvlogo.png")
logo = cv2.resize(logo, (logo.shape[0] // 2, logo.shape[1] // 2))
print(logo.shape)

logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(logo_gray, 10, 255, cv2.THRESH_BINARY)
roi = mushroom[:logo.shape[0], :logo.shape[1]]
bg = cv2.bitwise_and(roi, roi, mask=cv2.bitwise_not(mask))
fg = cv2.bitwise_and(logo,logo,mask=mask)

combined = cv2.add(bg,fg)
mushroom[:combined.shape[0],:combined.shape[1]]=combined


cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
while True:
    cv2.imshow("Image", mushroom)
    key = cv2.waitKey(1)
    if chr(key & 0xFF) == "q":
        break
cv2.destroyAllWindows()
