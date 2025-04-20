import cv2


cv2.namedWindow('Camera', cv2.WINDOW_KEEPRATIO)
cam = cv2.VideoCapture(0)
print(cv2.getBuildInformation())
while cam.isOpened():
    ret, frame = cam.read()
    cv2.imshow('Camera', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()


import cv2

# Создаем окно
cv2.namedWindow('Camera', cv2.WINDOW_KEEPRATIO)

# Указываем номер камеры, которая используется iVCam
cam = cv2.VideoCapture(2)  # Обычно iVCam используется на камере с индексом 1 (если это первая камера в системе)

# Проверяем успешность захвата
if not cam.isOpened():
    print("Ошибка: не удалось открыть камеру")
    exit()

while cam.isOpened():
    ret, frame = cam.read()
    
    if not ret:
        print("Ошибка при захвате кадра")
        break
    
    # Показываем изображение в окне
    cv2.imshow('Camera', frame)

    # Ожидаем нажатия клавиши 'q' для выхода
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# Освобождаем ресурсы
cam.release()
cv2.destroyAllWindows()
