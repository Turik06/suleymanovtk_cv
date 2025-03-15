import numpy as np
import matplotlib.pyplot as plt

# image = np.load("files/ex6npy.txt")
# print(image.shape)
# plt.imshow(image)
# plt.show()


# Внешние углы

external = np.array([
    [[0,0],[0,1]],
    [[0,0],[1,0]],
    [[0,1],[0,0]],
    [[1,0],[0,0]],
    
])

internal  = np.logical_not(external)

external_1 = np.array([[[1, 0], [0, 1]], [[0, 1], [1, 0]]])
# np.diag([1,1,1,1]).reshape(4,2,2)

def match(sub,mask):
    for mask in mask:
        if np.all(sub==mask):
            return True
    return False


def count_objects(image):
    E = 0

    for y in range(0,image.shape[0]-1):
        for x in range(0,image.shape[1]-1):
            sub = image[y:y+2,x:x+2]
            if match(sub,external):
                E+=1
            elif match(sub,internal):
                E-=1
            elif match(sub,external_1):
                E+=2

    return E/4
image = np.load("files/cex2npy.txt")
print(image.shape)
plt.imshow(image)
plt.show()
print(sum([count_objects(image[:,:,i]) for i in range(image.shape[2])]))
