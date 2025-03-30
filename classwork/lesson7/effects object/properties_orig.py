import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label,regionprops

image = np.zeros((100,100))

image[15:35,15:35] = 1
image[50:85,50:85]= 1
image[60:65,60:65]= 0

labeled = label(image)
regoins = regionprops(labeled)
print(regoins[0].area)
print(regoins[1].perimeter)
print(regoins[0].centroid)
print(regoins[0].centroid_local)

plt.imshow(regoins[1].image)
plt.show()