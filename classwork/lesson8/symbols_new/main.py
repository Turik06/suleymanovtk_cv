import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import regionprops,label
from skimage.morphology import binary_dilation
from pathlib import Path

def count_holes(region):
    shape = region.image.shape
    new_image = np.zeros((shape[0]+2,shape[1]+2))
    new_image[1:-1,1:-1] = region.image
    new_image = np.logical_not(new_image)
    labeled = label(new_image)
    return np.max(labeled)-1

def count_vlines(region):
    return np.all(region.image,axis = 0).sum()

def count_lgr_vlines(region):
    x = region.image.mean(axis =0 ) ==1
    return np.sum(x[:len(x)//2])>np.sum(x[len(x)//2:])

def recognize(region):
    if np.all(region.image):
        return "-"
    else: 
        holes = count_holes(region)
        if holes ==2:
            vlines = count_vlines(region)
            flag_lr = count_lgr_vlines(region)
            cy,cx = region.centroid_local
            cx/=region.image.shape[1]
            
            if flag_lr and cx<0.44:
                return "B"
            return "8"
        elif holes == 1:
            cy,cx = region.centroid_local
            cx/=region.image.shape[1]
            cy/=region.image.shape[0]
            if abs(cx-cy)< 0.03:
                return "0"
            return "A"
            
        else: 
            if count_vlines(region) >=3:
                return "1"
            else:
                if region.eccentricity < 0.4:
                    return "*"
                inv_image = ~region.image
                inv_image = binary_dilation(inv_image, np.ones((2, 2)))
                labeled = label(inv_image, connectivity=1)
                match np.max(labeled):
                    case 2: return "/"
                    case 4: return "X"
                    case _: return "W"


            
    return "#"

symbols= plt.imread(Path(__file__).parent/"symbols.png")[:, :, :-1]

gray = symbols.mean(axis=2)
binary = gray > 0
labeled = label(binary)
regions = regionprops(labeled)

result = {}
out_path = Path(__file__).parent/"out"
out_path.mkdir(exist_ok=True)
plt.figure()
for i,region in enumerate(regions):
    print(f"{i+1}/{len(regions)}")
    symbol = recognize(region)
    if symbol not in result:
        result[symbol]=0
    result[symbol]+=1
    plt.cla()
    plt.title(symbol)
    plt.imshow(region.image)
    plt.savefig(out_path/f"{i:03d}.png")


print(result)
