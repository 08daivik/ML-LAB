'''
Surface plot 

import matplotlib.pyplot as plt
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D

x=y=np.linspace(-3,3,30)
x,y=np.meshgrid(x,y)
z=x**2+y**2
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot_surface(x,y,z,cmap='viridis')
plt.show()
'''

#BFS

from queue import PriorityQueue

graph={'S':['A','B'],'A':['G'],'B':['G'],'G':[]}
h={'S':3,'A':2,'B':1,'G':0}

def bfs(start,goal):
    pq=PriorityQueue()
    pq.put((h[start],start))

    while not pq.empty():
        _, node=pq.get()
        print("Visited : ",node)

        if(node==goal):
            break

        for n in graph[node]:
            pq.put((h[n],n))

bfs('S','G')

