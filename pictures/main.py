import cv2
import numpy as np


lower = np.array([10, 150, 150])
upper = np.array([20, 255, 255])

img = cv2.imread("suleymanov.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, lower, upper)
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnt_tpl = max(contours, key=cv2.contourArea)

vid = cv2.VideoCapture("output.avi")
thresh = 0.01
c = 0

while True:
    ret, frame = vid.read()
    if not ret:
        break

    hsv    = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask   = cv2.inRange(hsv, lower, upper)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    found_cnt = None
    for cnt in contours:
        score = cv2.matchShapes(cnt_tpl, cnt, cv2.CONTOURS_MATCH_I1, 0.0)
        if score < thresh:
            found_cnt = cnt
            break

    if found_cnt is not None:
        c += 1

vid.release()
print(c)

