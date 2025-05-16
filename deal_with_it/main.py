import cv2 
import numpy as np

def censor(image, size=(5,5)):
    result = np.zeros_like(image)
    stepy = result.shape[0] // size[0]
    stepx = result.shape[1] // size[1]
    for y in range(0, image.shape[0], stepy):
        for x in range(0, image.shape[1], stepx):
            for k in range(image.shape[2]):
                result[y:y+stepy, x:x+stepx, k] = np.mean(image[y:y+stepy, x:x+stepx, k])
    return result

cv2.namedWindow("Camera", cv2.WINDOW_NORMAL)

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_AUTO_EXPOSURE, 3)
capture.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)

face_cascade = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade-eye.xml")


glasses = cv2.imread("deal-with-it.png")

while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        break

    blurred = cv2.GaussianBlur(frame, (7, 7), 0)
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    centroids = []
    points = []

    faces = eye_cascade.detectMultiScale(gray, scaleFactor=2.6, minNeighbors=20)
    for (x, y, w, h) in faces[:2]:
        centroids.append([x + w / 2, y + h / 2])
        points.append(x)
        points.append(x + w)

    if len(centroids) == 2:
        x = int((centroids[0][0] + centroids[1][0]) // 2)
        y = int((centroids[0][1] + centroids[1][1]) // 2)

        width = max(points) - min(points)
        k = width / glasses.shape[1]

        new_w = int(glasses.shape[1] * k) // 2 * 2
        new_h = int(glasses.shape[0] * k) // 2 * 2

        glasses_resized = cv2.resize(glasses, (new_w, new_h))

       
        lower = np.array([230, 230, 230])   
        upper = np.array([255, 255, 255])  
        mask_bg = cv2.inRange(glasses_resized, lower, upper) 
        mask_fg = cv2.bitwise_not(mask_bg) 

        y1 = y - new_h // 2
        y2 = y + new_h // 2
        x1 = x - new_w // 2
        x2 = x + new_w // 2

        if y1 >= 0 and y2 <= frame.shape[0] and x1 >= 0 and x2 <= frame.shape[1]:
            roi = frame[y1:y2, x1:x2]

            mask_fg_rgb = cv2.merge([mask_fg, mask_fg, mask_fg])
            mask_bg_rgb = cv2.merge([mask_bg, mask_bg, mask_bg])

            fg = cv2.bitwise_and(glasses_resized, mask_fg_rgb)
            bg = cv2.bitwise_and(roi, mask_bg_rgb)

            combined = cv2.add(bg, fg)
            frame[y1:y2, x1:x2] = combined

    key = chr(cv2.waitKey(1) & 0xFF)
    if key == "q":
        break

    cv2.imshow("Camera", frame)

capture.release()
cv2.destroyAllWindows()
