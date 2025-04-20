import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
from skimage.morphology import binary_erosion
from skimage.color import rgb2hsv
from collections import defaultdict


image = plt.imread('balls.png')

gray = image.mean(axis=2)
binary = gray > 0
labeled = label(binary)
regions = regionprops(labeled)
# print(regions[124].eccentricity)
# print(regions[120].eccentricity)

c = 0
colors = []
for region in regions:
    if region.eccentricity == 0.0:
        c += 1
        y, x = region.centroid
        colors.append(rgb2hsv(image[int(y), int(x)])[0])
    else:
        c += 2
        coords = region.coords
        region_colors = image[coords[:, 0], coords[:, 1]]        
        unique_colors = np.unique(region_colors, axis=0)
        colors.append(rgb2hsv(unique_colors[0])[0])
        colors.append(rgb2hsv(unique_colors[1])[0])


print(c)
print(colors)

# colors = np.unique(image)
# print(colors.shape)



plt.figure()
d = np.diff(sorted(colors))
pos = np.where(d > np.std(d)*2)
print(len(pos[0]) + 1)
plt.plot(np.diff(sorted(colors)), "-o")
plt.show()
plt.figure()
plt.subplot(121)
plt.imshow(image)
plt.subplot(122)
plt.imshow(labeled)
plt.show()


