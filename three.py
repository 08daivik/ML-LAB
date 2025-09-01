'''
Contour plot

import matplotlib.pyplot as plt
import numpy as np

x=y=np.linspace(-2,2,30)
x,y=np.meshgrid(x,y)
z=x**2 + y**2
plt.contour(x,y,z)
plt.title("Contour plot")
plt.show()
'''

#A* search

from queue import PriorityQueue

graph={'S':[('A',1),('B',2)],'A':[('G',3)],'B':[('G',1)],'G':[]}
h={'S':4,'A':2,'B':1,'G':0}

def astar(start,goal):
    pq=PriorityQueue()
    pq.put((0,start))
    cost={start:0}

    while not pq.empty():
        _, node=pq.get()
        print("Visited ",node)

        if(node==goal):
            break

        for n,c in graph[node]:
            new_cost=cost[node]+c
            if n not in cost or new_cost<cost[n]:
                cost[n]=new_cost
                pq.put((cost[n]+h[n],n))


astar('S','G')