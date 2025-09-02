# Agglomerative Clustering with Single-Linkage & Complete-Linkage
# Reads dataset from CSV file instead of sklearn dataset

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

df = pd.read_csv("data.csv")  


data = df.iloc[:, :-1].values  

def proximity_matrix(data):
    n = data.shape[0]
    proximity_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            proximity_matrix[i, j] = np.linalg.norm(data[i] - data[j])
            proximity_matrix[j, i] = proximity_matrix[i, j]
    return proximity_matrix

def plot_dendrogram(data, method):
    linkage_matrix = linkage(data, method=method)
    dendrogram(linkage_matrix)
    plt.title(f"Dendrogram - {method.capitalize()} Linkage")
    plt.xlabel("Data Points")
    plt.ylabel("Distance")
    plt.show()

print("Proximity Matrix:")
print(proximity_matrix(data))

plot_dendrogram(data, 'single')    
plot_dendrogram(data, 'complete')  
