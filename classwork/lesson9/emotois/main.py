import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import perimeter, regionprops, label

#ТОКА В EXTRACTOR
def extractor(region):
    area = region.area / region.image.size
    cy, cx = region.centroid_local
    cy /= region.image.shape[0]
    cx /= region.image.shape[1]
    perimeter = region.perimeter / region.image.size
    eccen = region.eccentricity / region.image.size
    ...
    return np.array([area, cy, cx, perimeter, eccen])


def norm_l1(v1, v2):
    return ((v1 - v2) ** 2).sum() ** 0.5


def classificator(v, templates):
    result = "_"
    min_dist = 10**16
    for key in templates:
        d = norm_l1(v, templates[key])
        if d < min_dist:
            result = key
            min_dist = d
    return result


alphabet = plt.imread("alphabet.png")[:, :, :-1]

gray = alphabet.mean(axis=2)
binary = gray > 0
labeled = label(binary)
regions = regionprops(labeled)
print(len(regions))

symbols = plt.imread("alphabet-small.png")[:, :, :-1]
gray = symbols.mean(axis=2)
binary = gray < 1
slabeled = label(binary)
sregions = regionprops(slabeled)
print(len(regions))

templates = {
    "A": extractor(sregions[2]),
    "B": extractor(sregions[3]),
    "8": extractor(sregions[0]),
    "0": extractor(sregions[1]),
    "1": extractor(sregions[4]),
    "W": extractor(sregions[5]),
    "X": extractor(sregions[6]),
    "*": extractor(sregions[7]),
    "-": extractor(sregions[9]),
    "/": extractor(sregions[8]),
}

print(templates)
# for i, region in enumerate(sregions):
#    v = extractor(region)
#    plt.subplot(2, 5, i + 1)
#    plt.title(classificator(v, templates))
#    plt.imshow(region.image)

result = {}
for region in regions:
    v = extractor(region)
    symbols = classificator(v, templates)
    result[symbols] = result.get(symbols, 0) + 1

print(result)
plt.show()