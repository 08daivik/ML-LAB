'''
Scatter plot 

import matplotlib.pyplot as plt
import numpy as np

x=np.random.rand(10)
y=np.random.rand(10)

plt.scatter(x,y)
plt.title("Scatter plot")
plt.show()

'''

#Hill Climbing alg

def f(x):
    return -x**2+4

x=float(input("Enter starting x : "))

for _ in range(50):
    next=x+0.1
    if(f(next)>f(x)):
        x=next

print("Best x = ",x," value = ",f(x))