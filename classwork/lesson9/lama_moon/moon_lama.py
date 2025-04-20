import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import regionprops,label
from skimage.filters import sobel, threshold_otsu
from skimage.morphology import binary_dilation
from pathlib import Path

image = plt.imread("lama-on-moon.png")[50:-50, 50:-50, :-1].mean(axis = 2)

s = sobel(image)

thresh = threshold_otsu(s)
s[s < thresh] = 0
s[s >= thresh] = 1

labeled = label(s)
regions = regionprops(labeled)
regions = sorted(regions, key = lambda item: item.perimeter)

plt.subplot(141)
plt.imshow(image)
plt.subplot(142)
plt.imshow(np.logical_or(labeled == regions[-1].label, labeled == regions[-2].label, labeled == regions[-4].label) )
plt.subplot(143)
plt.imshow(s)
plt.subplot(144)
plt.imshow(labeled)
plt.show()
