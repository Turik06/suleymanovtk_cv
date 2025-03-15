import numpy  as np
import random
import matplotlib.pyplot as plt
# print(np.arange(-5,5,1))
# # print(np.linspace(-3.14,3.14,5))
# # print(np.zeros((5,5)))
# # print(np.ones((2,3)))
# # # print(np.eye(4))
# # print(np.diag(np.arange(10)))
# print(np.meshgrid(range(5),range(5)))
# # array=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# # print(array[0])
# arr=np.random.randint(0,20,20)
# mask=arr%2==0
# # print(arr[mask])
# # arr=np.array([[1,2,3,4,5],[1,2,3,4,5]])
# # print(np.sum(arr,axis=1))
# arr=np.arange(15).reshape(5,3)
# # print(arr)
# plt.figure(1)
# plt.subplot(121)
# plt.plot([1,2,3])
# plt.subplot(122)
# plt.plot([3,2,1])
# # plt.show()
# plt.figure()
# plt.plot([3,5,2,1,5,7],[3,5,2,1,5,7])
# plt.show()
# a,b,c=3,2,1
# x= np.arange(-10,10+0.2,0.2)
# y=a+b*x+c
# ys=[]
# for i in range(1,6):
#     ys.append(x**i)
# plt.figure(figsize=(15,12))
# plt.subplot(121)
# plt.plot(x,y)
# plt.subplot(122)
# for i,y in enumerate(ys):
#     plt.plot(x,y,label=f"$x^{i}$")
# plt.legend()
# plt.grid()
# plt.tight_layout()
# plt.show()