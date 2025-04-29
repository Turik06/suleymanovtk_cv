import numpy as np 
import matplotlib.pyplot as plt
from skimage.measure import regionprops, label
from skimage.filters import sobel, threshold_otsu
from scipy.ndimage import binary_fill_holes

def find_pencil(region, size):
    h, w = region.image.shape
    minr, minc, maxr, maxc = region.bbox
    y, x = region.centroid
    y_local = y - minr
    x_local = x - minc
    x_norm = x_local / w
    y_norm = y_local / h

    center_ok = (0.4 < x_norm < 0.6) and (0.4 < y_norm < 0.6)

    diag = (h**2 + w**2) ** 0.5
    size_ok = (diag > size / 2) and (diag < size)

    perim_ratio = region.perimeter / diag
    shape_ok = 2.48 < perim_ratio < 5.52

    long_boi = (region.perimeter ** 2) / region.area > 33.33

    return center_ok and size_ok and shape_ok and long_boi

count_all = 0
for i in range(1, 13):
    image = plt.imread(f"./images/img ({i}).jpg").mean(axis=2)
    s = sobel(image)

    thresh = threshold_otsu(s) / 2
    s[s < thresh] = 0
    s[s >= thresh] = 1

    s = binary_fill_holes(s, np.ones((3, 3)))
    labeled = label(s)
    regions = regionprops(labeled)
    regions = sorted(regions, key=lambda item: item.perimeter)

    count = 0
    size = np.min(labeled.shape)

    for region in regions:
        if find_pencil(region, size):
            count += 1

    print(f'На {i} изображении {count} карандашей')
    count_all += count

print(f'На всех изображениях {count_all} карандашей')
