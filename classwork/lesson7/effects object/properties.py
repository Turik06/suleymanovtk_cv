# # ЦЕНТР ТЯЖЕСТИ
# import numpy as np
# import matplotlib.pyplot as plt
# from collections import defaultdict

# def area(labeled, lbl):
#     return np.sum(labeled == lbl)

# def centroid(labeled,label):
#     pos_y,pos_x=np.where(labeled==lbl)
#     cy= pos_y.mean()
#     cx= pos_x.mean()
#     return cy,cx

# def neighbours4(y,x):
#     return (y-1,x),(y+1,x),(y,x-1),(y,x+1)
# def neighboursX(y,x):
#     return (y-1,x+1),(y+1,x+1),(y+1,x-1),(y-1,x-1)

# def neighbours8(y,x):
#     return neighbours4(y,x)+neighboursX(y,x)

# def boundaries(labeled,lbl,connectivity= neighbours8):
#     pos = np.whhere(labeled==lbl)
#     bounds=[]
#     for y ,x in zip(*pos):
#         for yn,xn in connectivity(y,x):
#             if yn <0 or yn> labeled.shape[0]-1:
#                 bounds.append((y,x))
#             elif xn< 0 or xn>labeled.shape[1]-1:
#                 bounds.append((y,x))
#             elif labeled([yn,xn])==0:
#                 bounds.append((y,x))
            
#     return bounds

# def draw_bounds(labeled,connectivity = neighbours8):
#     result = labeled.copy()
#     for i in range(1,labeled.max()+1):
#         bounds = boundaries(labeled,i,connectivity)
#         for y,x in bounds:
#             result[y,x]+=1

#     return result



# LB = np.zeros((16, 16), dtype="int")
# LB[4:, :4] = 2

# LB[3:10, 8:] = 1
# LB[[3, 4, 3], [8, 8, 9]] = 0
# LB[[8, 9, 9], [8, 8, 9]] = 0
# LB[[3, 4, 3], [-2, -1, -1]] = 0
# LB[[9, 8, 9], [-2, -1, -1]] = 0

# LB[12:-1, 6:9] = 3
# plt.imshow(LB)
# for lbl in range(1,np.max(LB)+1):
#     print(area(LB,lbl))
#     cy,cx = centroid(LB,lbl)
#     plt.scatter([cx],[cy])

# # areas = defaultdict(lambda: 0)
# # for lbl in range(1, np.max(LB) + 1):
# #     areas[area(LB, lbl)] += 1
# # print(areas)

# print(draw_bounds(LB))
# plt.imshow(LB)
# plt.show()




import numpy as np
import matplotlib.pyplot as plt

def area(labeled, lbl):
    return (labeled == lbl).sum()

def centroid(labeled ,lbl):
    pos_y, pos_x = np.where(labeled == lbl)
    cy = pos_y.mean()
    cx = pos_x.mean()
    return cy, cx

def neighbours4(y, x):
    return(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)

def neighboursX(y, x):
    return (y - 1, x + 1), (y + 1, x + 1), (y + 1, x - 1), (y - 1, x - 1)

def neighbours8(y, x):
    return neighbours4(y, x) + neighboursX(y, x)

def boundaries(labeled, lbl, connectivity = neighbours8):
    pos = np.where(labeled == lbl)
    bounds = []
    for y, x in zip(*pos):
        for yn, xn in connectivity(y, x):
            if yn < 0 or yn > (labeled.shape[0] - 1):
                bounds.append((y, x))
                break
            elif xn < 0 or xn > (labeled.shape[1] - 1):
                bounds.append((y, x))
                break
            elif labeled[yn, xn] == 0:
                bounds.append((y, x))
                break
    return bounds

def diatance(px1,px2):
    return ((px1[0]-px2[0]) **2 + (px1[1]-px2[1])**2)**0.5

def std_radial(labeled,lbl,connectivity=neighbours8):
    r,c = centroid(labeled,lbl)
    bounds = boundaries(labeled,lbl,connectivity)
    K = len(bounds)
    sr = 0 
    rd = radial_distance(labeled,lbl,connectivity)
    for rk,ck in bounds:
        sr+=(diatance((r,c),(rk,ck))-rd)**2
    return (sr/K)**0.5

def radial_distance(labeled,lbl,connectivity=neighbours8):
    r,c = centroid(labeled,lbl)
    bounds = boundaries(labeled,lbl,connectivity)
    K = len(bounds)
    rd=0
    for rk,ck in bounds:
        rd+=diatance((r,c),(rk,ck))
    return rd/K

def circularity_std(labeled,lbl,connectivity = neighbours8):
    return radial_distance(labeled,lbl,connectivity)/std_radial(labeled,lbl,connectivity)

def draw_bounds(labeled, connectivity = neighbours8):
    result = labeled.copy()
    for i in range(1, labeled.max()+1):
        bounds = boundaries(labeled, i, connectivity)
        for y, x in bounds:
            result[y, x] += 1
    return result

def perimetr(labeled,lbl,connectivity=neighbours8):
    return len(boundaries(labeled,lbl,connectivity))

def reug(labeled,lbl,connectivity = neighbours8):
    return (perimetr(labeled,lbl,connectivity)**2)/area(labeled,lbl)

LB = np.zeros((16, 16), dtype="int")
LB[4:, :4] = 2

LB[3:10, 8:] = 1
LB[[3, 4, 3], [8, 8, 9]] = 0
LB[[8, 9, 9], [8, 8, 9]] = 0
LB[[3, 4, 3], [-2, -1, -1]] = 0
LB[[9, 8, 9], [-2, -1, -1]] = 0

LB[12:-1, 6:9] = 3

plt.imshow(LB)

for lbl in range(1, np.max(LB) + 1):
    # print(area(LB, lbl))
    cy, cx = centroid(LB, lbl)
    plt.scatter([cx], [cy])
    # print(f"Perimetr{(perimetr(LB,lbl,neighbours8))}")
    # print(f"Perimetr{(reug(LB,lbl,neighbours4))}")
    print(f"CERCULARITY  {circularity_std(LB,lbl,connectivity=neighbours4)}")

# print((draw_bounds(LB)))

# plt.show()
# plt.imshow(draw_bounds(LB))
# plt.show()
