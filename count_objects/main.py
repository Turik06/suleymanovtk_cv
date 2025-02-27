import numpy as np
import matplotlib.pyplot as plt

# Загружаем изображение и создаем копию, преобразуя ее в булев массив
image = np.load("example1.npy")
image_copy = (image != 0).astype(bool)  # Работаем с копией

print(image_copy.shape)

# Приведение к float перед отображением.
plt.imshow(image_copy.astype(float), cmap="gray")
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
    for y in range(image.shape[0] - 1):
        for x in range(image.shape[1] - 1):
            sub = image[y : y + 2, x : x + 2]  
            if match(sub, external):
                E += 1
            elif match(sub, internal):
                E -= 1
            elif match(sub, cross):
                E += 2
    return E / 4


# Проверка размерности изображения перед подсчетом
if len(image_copy.shape) == 3:
    print(sum(count_objects(image_copy[:, :, i]) for i in range(image_copy.shape[2])))
else:
    print(count_objects(image_copy))
