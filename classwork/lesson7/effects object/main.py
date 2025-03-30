import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label
from collections import defaultdict

def area(labeled, lbl):
    return np.sum(labeled == lbl)

coins = np.load("coins.npy")
labeled = label(coins)

areas = defaultdict(lambda: 0)
for lbl in range(1, np.max(labeled) + 1):
    areas[area(labeled, lbl)] += 1

nominals = np.array([1, 2, 5, 10])

sorted_areas = np.array(sorted(areas.items()))

if len(sorted_areas) == len(nominals):
    a= nominals * sorted_areas[:, 1]
    print(sum(a))
else:
    print("Количество различных площадей не совпадает с числом номиналов!")

plt.imshow(coins)
plt.show()


