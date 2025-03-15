# x=np.linspace(-4*np.pi,4*np.pi,100)
# sn=4* np.sin(x)
# cs=np.cos(2*x)
# plt.plot(x,sn,label="sin")
# plt.plot(x,cs,label="cos")
# plt.legend()
# plt.show()
import numpy  as np
import random
import matplotlib.pyplot as plt
from scipy.datasets import face 

def convolve(image:np.ndarray, mask:np.ndarray) ->np.ndarray:
    result: np.ndarray = np.zeros(image.shape)
    for i in range(1,image.shape[0]-1):
        for j in range(1,image.shape[1]-1):
            sub_image = image[i-1:i+2,j-1:j+2]
            value: int = np.sum(sub_image * mask) 
            result[i,j]=value

    return result[1:-1,1:-1]

image= face(gray=True)
maskc=np.array([[2,-1,-1],[-1,2,-1],[-1,-1,2]])
resultc = convolve(image,maskc)
maskv=np.array([[-1,-1,2],[-1,2,-1],[2,-1,-1]])
resultv = convolve(image,maskv)

plt.subplot(121)
plt.imshow(resultc)
plt.clim(0,50)
plt.subplot(122)
plt.imshow(resultv)
plt.clim(0,50)
plt.show()
print(image.shape)
print(image.dtype)
