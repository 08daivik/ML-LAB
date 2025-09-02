'''
Heatmap

import seaborn as sns
import numpy as np
import matplotlib as plt

data=np.random.rand(4,4)
sns.heatmap(data,annot=True)
plt.title("Heatmap")
plt.show()
'''

#min-max

def minmax(values,is_max):
    a=values[0:2]
    b=values[2:4]

    return max(min(a),min(b)) if is_max else min(max(a),max(b))

vals=list(map(int,input("Enter 4 value ").split()))
print("result: ",minmax(vals,True))

