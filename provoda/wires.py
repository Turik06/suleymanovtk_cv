import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label
from skimage.morphology import (binary_closing,binary_opening,binary_dilation,binary_erosion)

files = ["wires1npy.txt","wires2npy.txt","wires3npy.txt","wires4npy.txt","wires5npy.txt","wires6npy.txt"]
erosion_kernel = np.ones((3, 1)) 

for file in files:
    data = np.load(file)

    labeled_wires = label(data)
    num_wires = np.max(labeled_wires)
    print(f"Файл: {file}, Обнаружено {num_wires} проводов на изображении.")

    for wire_label in range(1,num_wires+1):
        current_wire_mask = (labeled_wires == wire_label)

        eroded_wire_mask = binary_erosion(current_wire_mask, erosion_kernel)

        wire_components_labeled = label(eroded_wire_mask)
        num_components = np.max(wire_components_labeled)

        if num_components > 1:
            print(f"  Провод {wire_label}: Порван на {num_components} частей .")
        elif num_components == 1:
            print(f"  Провод {wire_label}: Целый ")
        else:
            print(f"  Провод {wire_label}: Уничтожен ")
    print("-" * 30) 
data = np.load("wires4npy.txt")
plt.imshow(data)
plt.show()