import numpy as np
import matplotlib.pyplot as plt
from skimage import draw
import random
from skimage.morphology import binary_dilation

def hist(arr):
    h=np.zeros(256)
    for v in arr.flatten():
        h[v] +=1
    return h

image = np.zeros((500,500),dtype="uint8")
image[:]=np.random.randint(0,50,image.size).reshape(image.shape)
rr,cc=draw.disk((150,150),75)
image[rr,cc]=  np.random.randint(40,80,len(rr))

rr,cc=draw.disk((350,350),85)
image[rr,cc]=  np.random.randint(70,120,len(rr))

binary = image.copy()
binary[binary<60]=0
binary[binary>0]=1

binary = binary_dilation(binary,np.ones((5,5)))

plt.subplot(131)
plt.imshow(image)
plt.subplot(132)
plt.plot(hist(image))
plt.subplot(133)
plt.imshow(binary)
plt.show()
