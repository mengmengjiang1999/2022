# import base64
# filepath_image = "./dijkstra.png"
# file_image = open(filepath_image, "rb")
# data_image = file_image.read()
# data_image = base64.b64encode(data_image)
# print(data_image)

import random
from xml.dom.minicompat import NodeList

from sklearn.utils import shuffle

N_max=6
N_min=5
W_min=1
W_max=20


DENSITY = 0.45

def gen_edges(N):
    # 随机生成边序列
    # edges := list[(int,int,int)]
    edges = []
    node_list = [i for i in range(1,N+1,1)]
    shuffle(node_list)
    for i in range(len(node_list)-1):
        w = random.randint(W_min, W_max)
        edges.append((node_list[i],node_list[i+1],w))
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i!=j:
                rnd = random.random()
                if rnd < DENSITY:
                    w = random.randint(W_min, W_max)
                    edges.append((i,j,w))
    S = 1
    T = N
    return edges, S, T

N = random.randint(N_min,N_max)

data = gen_edges(N)

print(data)