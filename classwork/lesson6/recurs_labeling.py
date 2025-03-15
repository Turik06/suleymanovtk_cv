import numpy as np
import matplotlib.pyplot as plt
import sys

# sys.setrecursionlimit(1500000)

image = np.zeros((20, 20), dtype="int32")

def fill(lb, label, y, x):
    lb[y, x] = label
    for ny, nx in neighbours4(y, x):
        if lb[ny, nx] == -1:
            fill(lb, label, ny, nx)

def recursive_labeling(image):
    label = 0
    lb = image * -1
    for y in range(lb.shape[0]):
        for x in range(lb.shape[1]):
            if lb[y, x] == -1:
                label += 1
                fill(lb, label, y, x)
    return lb

def neighbours4(y, x):
    return (y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)

def neighbours2(y, x):
    return (y - 1, x), (y, x - 1)

def find(label, linked):
    j = label
    while linked[j] != 0:
        j = linked[j]
    return j

def union(label1, label2, linked):
    j = find(label1, linked)
    k = find(label2, linked)
    if j != k:
        linked[k] = j

def two_pass(image):
    labeled = np.zeros_like(image)
    linked = np.zeros(image.size // 2, dtype="uint")
    label = 0
    for y in range(1, image.shape[0]):
        for x in range(1, image.shape[1]):
            if image[y, x] != 0:
                nbs = neighbours2(y, x)
                left = labeled[nbs[0]]
                top = labeled[nbs[1]]
                if left == 0 and top == 0:
                    label += 1
                    m = label
                else:
                    m = min([left, top])
                    if m == 0:
                        m = max([left, top])
                labeled[y, x] = m
                for n in nbs:
                    if labeled[n] != 0:
                        lb = labeled[n]
                        if lb != m:
                            union(m, lb, linked)
    for y in range(1, image.shape[0]):
        for x in range(1, image.shape[1]):
            if image[y, x] != 0:
                lbl = find(labeled[y, x], linked)
                if lbl != labeled[y, x]:
                    labeled[y, x] = lbl

    return labeled


def renumber_labels(labeled):
    unique_labels = np.unique(labeled)[1:]
    for new_label, old_label in enumerate(unique_labels, start=1):
        labeled[labeled == old_label] = new_label  
    return labeled

image[1:-1, -2] = 1
image[1, 1:5] = 1
image[1, 7:12] = 1
image[2, 1:3] = 1
image[2, 6:8] = 1
image[3:4, 1:7] = 1
image[7:11, 11] = 1
image[7:11, 14] = 1
image[10:15, 10:15] = 1
image[5:10, 5] = 1
image[5:10, 6] = 1


labeled = two_pass(image)


labeled = renumber_labels(labeled)


plt.imshow(labeled)
plt.show()
