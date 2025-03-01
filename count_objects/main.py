import numpy as np
import matplotlib.pyplot as plt

# Загружаем изображение и создаем копию, преобразуя ее в булев массив
image1 = np.load("example1.npy")
image2 = np.load("example2.npy")
image_copy1 = (image1 != 0).astype(bool)  # Работаем с копией
image_copy2 = (image2 != 0).astype(bool)  # Работаем с копией

print(image_copy1.shape)
print(image_copy2.shape)

# Приведение к float перед отображением.
plt.imshow(image_copy1.astype(float), cmap="gray")
plt.show()
plt.imshow(image_copy2.astype(float), cmap="gray")
plt.show()


external = (np.diag([1, 1, 1, 1]).reshape(4, 2, 2))
internal = np.logical_not(external)
cross = (np.array([[[1, 0], [0, 1]], [[0, 1], [1, 0]]]))


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
if len(image_copy1.shape) == 3:
    print(sum(count_objects(image_copy1[:, :, i]) for i in range(image_copy1.shape[2])))
else:
    print(count_objects(image_copy1))
if len(image_copy2.shape) == 3:
    print(sum(count_objects(image_copy2[:, :, i]) for i in range(image_copy2.shape[2])))
else:
    print(count_objects(image_copy2))