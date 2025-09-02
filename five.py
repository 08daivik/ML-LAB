'''
box plot

import matplotlib.pyplot as plt
import numpy as np

data=list(map(int,input("ENter values").split()))
plt.boxplot(data)
plt.title("Boxplot")
plt.show()
'''

#alpha beta

def alphabeta(values):
    a=min(values[0],values[1])
    b=min(values[2],values[3])

    return max(a,b)

vals=list(map(int,input("Enter numbers").split()))
print("result : ",alphabeta(vals))