
# 1680
import mss
import numpy as np  
import cv2 
import pyautogui 
import time 

# --- Координаты захвата экрана ---
Y1, Y2 = 340, 480
X1, X2 = 6, 250
MONITOR = {"top": Y1, "left": X1, "width": X2 - X1, "height": Y2 - Y1}

# --- Относительные координаты ROI (областей интереса) ---
CACTUS_Y_FRAC_START = 0.85
CACTUS_Y_FRAC_END = 0.95
PTERO_Y_FRAC_START = 0.60
PTERO_Y_FRAC_END = 0.70 
 
#  --- ROI и пороги срабатывания ---
ROI_WIDTH = 54 
BASE_CACTUS_X_START = 131
BASE_PTERO_X_START = 130 
CACTUS_THRESHOLD = 0
PTERO_THRESHOLD = 1

# --- Базовые тайминги действий (будут делиться на speed_factor) ---
BASE_DUCK_DURATION = 0.2
BASE_DELAY_BEFORE_FAST_DESCEND = 0.16
BASE_FAST_DESCEND_DURATION = 0.038  
 
#  --- Логика скорости игры ---
SCORE_SPEED_FACTOR = 45000.0
MIN_SLEEP_DURATION = 0.001

# --- Отладка ---
SHOW_DEBUG_WINDOWS = True  # Установите в True для отображения окон отладки

# --- Функции действий ---
def jump(speed_factor):
    delay_before = max(MIN_SLEEP_DURATION, BASE_DELAY_BEFORE_FAST_DESCEND / speed_factor)
    descend_duration = max(MIN_SLEEP_DURATION, BASE_FAST_DESCEND_DURATION / speed_factor)

    pyautogui.press('space')
    time.sleep(delay_before)
    pyautogui.keyDown('down')
    time.sleep(descend_duration)
    pyautogui.keyUp('down')


def duck(speed_factor):
    duck_duration = max(MIN_SLEEP_DURATION, BASE_DUCK_DURATION / speed_factor)
    pyautogui.keyDown('down')
    time.sleep(duck_duration)
    pyautogui.keyUp('down')


with mss.mss() as sct:
    score = 0
    last_time = time.time()

    print("Запуск Dino Bot. Нажмите 'q' в окне для выхода, 'p' — пауза.")

    while True:
        sct_img = np.array(sct.grab(MONITOR))
        frame = cv2.cvtColor(sct_img, cv2.COLOR_BGRA2BGR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

        # Рассчёт фактора скорости
        speed_factor = 1 + (score / SCORE_SPEED_FACTOR)
        speed_factor = min(speed_factor, 3.0)
        speed_factor = max(speed_factor, 1.0)

        window_height = Y2 - Y1
        window_width = X2 - X1

        # Вертикальные границы ROI
        cactus_y_start = int(window_height * CACTUS_Y_FRAC_START)
        cactus_y_end = int(window_height * CACTUS_Y_FRAC_END)
        ptero_y_start = int(window_height * PTERO_Y_FRAC_START)
        ptero_y_end = int(window_height * PTERO_Y_FRAC_END)

        # Горизонтальные границы ROI смещаем дальше от динозавра пропорционально speed_factor
        cactus_x_start = min(window_width - ROI_WIDTH, int(BASE_CACTUS_X_START * speed_factor))
        cactus_x_end = cactus_x_start + ROI_WIDTH

        ptero_x_start = min(window_width - ROI_WIDTH, int(BASE_PTERO_X_START * speed_factor))
        ptero_x_end = ptero_x_start + ROI_WIDTH

        # Извлечение ROI
        roi_cactus = binary[cactus_y_start:cactus_y_end, cactus_x_start:cactus_x_end]
        roi_ptero = binary[ptero_y_start:ptero_y_end, ptero_x_start:ptero_x_end]

        white_cactus = cv2.countNonZero(roi_cactus)
        white_ptero = cv2.countNonZero(roi_ptero)

        if white_cactus > CACTUS_THRESHOLD:
            jump(speed_factor)
        elif white_ptero > PTERO_THRESHOLD:
            duck(speed_factor)

        if SHOW_DEBUG_WINDOWS:
            debug_frame = frame.copy()
            cv2.rectangle(debug_frame, (cactus_x_start, cactus_y_start), (cactus_x_end, cactus_y_end), (0, 255, 0), 2)
            cv2.rectangle(debug_frame, (ptero_x_start, ptero_y_start), (ptero_x_end, ptero_y_end), (255, 0, 0), 2)
            cv2.putText(debug_frame, f'C: {white_cactus}', (cactus_x_start, cactus_y_start - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)
            cv2.putText(debug_frame, f'P: {white_ptero}', (ptero_x_start, ptero_y_start - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)
            cv2.imshow("Game Frame", debug_frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('p'):
            print("Пауза. Нажмите Enter для продолжения...")
            input()

        now = time.time()
        score += (now - last_time) * 100
        last_time = now

    cv2.destroyAllWindows()
    print(f"Финальный счёт: {int(score)}")
