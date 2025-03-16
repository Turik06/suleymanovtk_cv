import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label
from skimage.morphology import binary_opening

data = np.load("stars.npy")
notstars = np.array([[1,1,1],
            [1,1,1]])

notstars_morfo = binary_opening(data,notstars)
labeled_notstars = label(notstars_morfo)

labeled_data=label(data)

print(f"Количество плюсов и крестиков: {np.max(labeled_data)-np.max(labeled_notstars)}")
