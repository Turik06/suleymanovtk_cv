import numpy as np
import matplotlib.pyplot as plt

# Загружаем изображение и сразу преобразуем его в булев массив, чтобы алгоритм мог работать с картинкой
image = (np.load("example2.npy") != 0).astype(bool)
print(image.shape)
plt.imshow(image)
plt.show()


external = (np.diag([1, 1, 1, 1]).reshape(4, 2, 2) != 0).astype(bool)
internal = np.logical_not(external)
cross = (np.array([[[1, 0], [0, 1]], [[0, 1], [1, 0]]]) != 0).astype(bool)


def match(a, masks):
    for mask in masks:
        if np.all(a == mask):
            return True
    return False

def count_objects(image):
    E = 0
    for y in range(0, image.shape[0] - 1):
        for x in range(0, image.shape[1] - 1):
            sub = image[y : y + 2, x : x + 2]  # Здесь image уже булевый
            if match(sub, external):
                E += 1
            elif match(sub, internal):
                E -= 1
            elif match(sub, cross):
                E += 2
    return E / 4

# print(count_objects(image)) #Для первого файла
print(sum([count_objects(image[:,:,i]) for i in range(image.shape[2])])) #Для второго файла
