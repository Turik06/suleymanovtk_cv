import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
from skimage.color import rgb2hsv

image = plt.imread('./balls_and_rects.png')

gray = image.mean(axis=2)
binary = gray > 0

labeled = label(binary)
regions = regionprops(labeled)

count_balls = 0
colors_balls = []
count_rects = 0
colors_rects = []

for region in regions:
    h, w = region.image.shape
    area = h * w
    is_rectangle_area = (region.area == area)
  
    ratio = region.minor_axis_length / region.major_axis_length
    is_circle_ratio = (ratio > 0.9)

    y, x = region.centroid
    hue = rgb2hsv(image[int(y), int(x)])[0]
 
    if is_circle_ratio and not is_rectangle_area:
        count_balls += 1
        colors_balls.append(hue)
    else:
        count_rects += 1
        colors_rects.append(hue)

colors_all = [rgb2hsv(image[int(r.centroid[0]), int(r.centroid[1])])[0] for r in regions]


print(f'Количество кругов: {count_balls}')
print(f'Количество прямоугольников: {count_rects}')
print(f'Количество всех фигур: {len(colors_all)}')

def analyze_shades(colors, std_mult=1.0, label_name=''):
    diffs = np.diff(sorted(colors))
    splits = np.where(diffs > np.std(diffs) * std_mult)[0]
    num_shades = len(splits) + 1
    print(f"\n{label_name} Оттенков: {num_shades}")
    prev = 0
    for i, split in enumerate(splits, start=1):
        count = split - prev + 1  
        print(f"Оттенок {i}: {count} объектов")
        prev = split + 1
    last_count = len(colors) - prev
    print(f"Оттенок {num_shades}: {last_count} объектов")

print("\nОбщие оттенки")
analyze_shades(colors_all, std_mult=1.0, label_name='Общие')
print("\nОттенки кругов")
analyze_shades(colors_balls, std_mult=2.0, label_name='Круги')
print("\nОттенки прямоугольников")
analyze_shades(colors_rects, std_mult=2.0, label_name='Прямоугольники')
