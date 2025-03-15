import numpy as np
import matplotlib.pyplot as plt

arr = np.array([[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,0,0],
                [0,0,0,0,1,1,1,1,0,0],
                [0,0,0,0,1,1,1,1,0,0],
                [0,0,0,1,1,1,1,1,0,0],
                [0,0,0,0,1,1,1,1,0,0],
                [0,0,0,1,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0]])

struct = np.ones((3, 3))
 
# Наращивание функция
def dilation(arr):
    result = np.zeros_like(arr)
    for y in range(1, arr.shape[0] - 1):
        for x in range(1, arr.shape[1] - 1):
            sub = np.logical_and(arr[y, x], struct)
            result[y - 1:y + 2, x - 1:x + 2] = np.logical_or(result[y - 1:y + 2, x - 1:x + 2], sub)
    return result

# операция эрозии (уменьшение)
def erosion(arr):
    result = np.zeros_like(arr)
    for y in range(1, arr.shape[0] - 1):
        for x in range(1, arr.shape[1] - 1):
            sub = arr[y-1:y+2,x-1:x+2]
            if np.all(sub == struct):
                result[y,x]= 1
    return result

# Операция замыкания
def closing(arr):
    return erosion(dilation(arr))

# Операция открытие 
def opening(arr):
    return dilation(erosion(arr))

plt.subplot(121)
plt.imshow(arr)
plt.subplot(122)
plt.imshow(closing(arr))
plt.show()
