import numpy as np
import matplotlib.pyplot as plt
from scipy.datasets import face

def translate(image,vector):
    translated = np.zeros_like(image)
    for y in range(0,image.shape[0]):
        for x in range(0,image.shape[1]):
            ny = y+ vector[0]
            nx = x+ vector[1]
            if ny >=image.shape[0] or nx>=image.shape[1]:
                continue
            if ny<0 or nx<0:
                continue
            translated[ny,nx] = image[y,x]
    return translated
    
image = face(gray=True)
image = translate(image,(50,50))
plt.imshow(image)
plt.show()


