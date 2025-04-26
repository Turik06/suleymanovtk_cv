import socket
import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops


def recvall(sock, n):
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    return data


host = "84.237.21.36"
port = 5152
beat = None

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))
    plt.ion()
    plt.figure()

    while beat != b"yep":
        sock.send(b"get")
        bts = recvall(sock, 40002)

        beat = b"nope"

        im1 = np.frombuffer(bts[2:40002], dtype="uint8").reshape(bts[0], bts[1])

        binary = im1 > 0
        labeled = label(binary)
        regions = regionprops(labeled)
        if len(regions) == 2:
            cy1, cx1 = regions[0].centroid
            cy2, cx2 = regions[1].centroid
            result = np.sqrt((cx2 - cx1)**2 + (cy2 - cy1)**2)

            sock.send(f"{result:.1f}".encode())
            print(sock.recv(10))
            sock.send(b"beat")
            beat = sock.recv(10)
            plt.clf()
            plt.subplot(121)
            plt.imshow(im1)
            plt.pause(1)

        

# with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
#     sock.connect((host,port))
#     beat = b"nope"
#     plt.ion()
#     plt.figure()

#     while beat!= b"yep":

#         sock.send(b"get")
#         bts = recvall(sock,80004)
#         print(len(bts))

#         im1 = np.frombuffer(bts[2:40002],
#                             dtype="uint8").reshape(bts[0],bts[1])
        
#         im2 = np.frombuffer(bts[40004:],
#                             dtype="uint8").reshape(bts[40002],bts[40003])
        
#         pos1 = np.unravel_index(np.argmax(im1),im1.shape)
#         pos2 = np.unravel_index(np.argmax(im2),im1.shape)
#         result= np.abs(np.array(pos1) - np.array(pos2))

#         sock.send(f"{result[0]} {result[1]}".encode())
#         print(sock.recv(10))
#         plt.clf()
#         plt.subplot(121)
#         plt.imshow(im1)
#         plt.subplot(122)
#         plt.imshow(im2)
#         plt.pause(1)

#         sock.send(b"beat")
#         beat = sock.recv(10)


