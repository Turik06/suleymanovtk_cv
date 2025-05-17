import cv2
import zmq
import numpy as np


host = "84.237.21.36"
port = 6002

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.SUBSCRIBE, b"")
socket.connect(f"tcp://{host}:{port}")

cv2.namedWindow("Client", cv2.WINDOW_GUI_NORMAL)
count = 0

while True:
    message = socket.recv()
    frame = cv2.imdecode(np.frombuffer(message, np.uint8), cv2.IMREAD_UNCHANGED)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    inv = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)[1]

    morf = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
    thresh = cv2.erode(inv, morf, iterations=3)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(frame, contours, -1, (255, 0, 0), 3, cv2.LINE_AA, hierarchy, 1)

    circle_count = 0

    for contour in contours:
        area = cv2.contourArea(contour)
        (x, y), radius = cv2.minEnclosingCircle(contour)
        center = (int(x), int(y))
        radius = int(radius)
        circle_area = np.pi * (radius ** 2)

        if circle_area == 0:
            continue

        cv2.circle(frame, center, radius, (0, 255, 255), 2)

        ratio = area / circle_area

        if 0.8 < ratio < 1.15:
            circle_count += 1

    count += 1
    key = chr(cv2.waitKey(1) & 0xFF)
    if key == "q":
        break
    cv2.putText(frame, f"Count {count}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0))
    cv2.putText(frame, f"squares {len(contours) - circle_count} circles {circle_count}", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0))
    cv2.imshow("Client", frame)
