
import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
from skimage.morphology import binary_erosion
from skimage.color import rgb2hsv
from pathlib import Path

def print_res(colors, pos):
    print('Количество оттенков: ' + str(len(pos[0]) + 1))
    print(f'Количество фигур 1 оттенка: {pos[0][0]}')
    for i in range(1,len(pos[0])):
        print(f'Количество фигур {i+1} оттенка: {pos[0][i]-pos[0][i-1]}')
    print(f'Количество фигур {len(pos[0])+1} оттенка: {len(colors) - pos[0][len(pos[0])-1]}')

img = plt.imread('balls_and_rects.png')

gray = img.mean(axis=2)
binary = gray > 0
mask = np.ones((7, 7))
labeled = label(binary)
regions = regionprops(labeled)

c_balls = 0
colors_balls = []
c_rects = 0
colors_rects = []
for i, region in enumerate(regions):
    if region.area!=region.image.shape[0]*region.image.shape[1]:
        c_balls += 1
        y, x = region.centroid
        colors_balls.append(rgb2hsv(img[int(y), int(x)])[0])
    else:
        c_rects += 1
        y, x = region.centroid
        colors_rects.append(rgb2hsv(img[int(y), int(x)])[0])
c = 0
colors = []
for i, region in enumerate(regions):
    c += 1
    y, x = region.centroid
    colors.append(rgb2hsv(img[int(y), int(x)])[0])
print(f'Количество кругов: {len(colors_balls)}')
print(f'Количество прямоугольников: {len(colors_rects)}')
print(f'Количество всех фигур: {len(colors)}')


d = np.diff(sorted(colors))
pos = np.where(d > np.std(d))
print('Всего:')
print_res(colors, pos)
print('\n')

d_balls = np.diff(sorted(colors_balls))
pos_balls = np.where(d_balls > np.std(d_balls) * 2)
print('Круги:')
print_res(colors_balls, pos_balls)
print('\n')

print('Прямоугольники:')
d_rects = np.diff(sorted(colors_rects))
pos_rects = np.where(d_rects > np.std(d_rects) * 2)

print_res(colors_rects, pos_rects)