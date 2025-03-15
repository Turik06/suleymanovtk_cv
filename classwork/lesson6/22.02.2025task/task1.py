import numpy as np
import matplotlib.pyplot as plt
from scipy.datasets import face
import random
# image = np.zeros((100,100))

# image[::2,::2]=1
# image[1::2,1::2]=1

# plt.imshow(image)
# plt.show()

# image= np.zeros((500,500))

# bs=25
# num = 0
# for y in range(0,image.shape[0],bs):
#     for x in range(0,image.shape[1],bs):
#         image[y:y+bs,x:x+bs] = num
#         num+=1

# plt.imshow(image)
# plt.show()


# image =np.ones((600,600))

# d= 250

# y= np.arange(600).reshape(600,1) - 300
# x = np.arange(600).reshape(1,600) - 300

# mask=x**2+y**2<(d/2)**2

# plt.imshow(mask)
# plt.show()


# def descritize(image,levels=2):
#     mn = image.min()
#     mx=np.max(image)
#     result = image.copy()
#     percent = (result - mn) / (mx- mn)
#     result = (percent * levels).astype("uint16")
#     return result


# image= face(gray=True)

# plt.imshow(descritize(image,16000))
# plt.show()



# def block_mean(image,ybc=10,xbc=10):
#     result=image.copy()
#     ybs= image.shape[0] //ybc
#     xbs = image.shape[1] // xbc
    
#     for y in range(0,image.shape[0],ybs):
#         for x in range(0,image.shape[1],xbs):
#             sub = image[y:y+ybs,x:x+xbs]
#             result[y:y+ybs,x:x+xbs]=sub.min()
#     return result

# image= face(gray=True)

# plt.imshow(block_mean(image,51,51))
# plt.show()

def mse(reference, noised):
    return ((reference - noised) ** 2).sum() / reference.size

def psnr(reference, noised):
    return 20 * np.log10(reference.max() / np.sqrt(mse(reference,noised)))

image = face(gray=True)
noised = image.copy()

noise_percent = 0.5
noised_pixels = int(noise_percent * image.size)

y_pos, x_pos = np.meshgrid(np.arange(image.shape[0]), np.arange(image.shape[1]))
y_pos = y_pos.flatten()
x_pos = x_pos.flatten()
pos = np.random.choice(np.arange(len(y_pos)), noised_pixels)
yn = y_pos[pos]
xn = x_pos[pos]
noised[yn, xn] = np.random.randint(0, 255, noised_pixels)

print(psnr(image,noised))
plt.figure()
plt.subplot(121)
plt.title("Original")
plt.imshow(image)
plt.subplot(122)
plt.title("Noised")
plt.imshow(noised)
plt.show()