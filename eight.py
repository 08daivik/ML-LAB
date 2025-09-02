# K-means Clustering on Iris Dataset (Reading from CSV)

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def kmeans_clustering():
   
    df = pd.read_csv("iris.csv")
    
    
    X = df.iloc[:, :-1].values  

    K = 3

   
    kmeans = KMeans(n_clusters=K, random_state=0)
    labels = kmeans.fit_predict(X)
    centroids = kmeans.cluster_centers_

    print("K-means Labels:\n", labels)
    print("\nK-means Centroids:\n", centroids)

    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=50)
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', color='red', s=200, label="Centroids")
    plt.xlabel('Sepal Length')
    plt.ylabel('Sepal Width')
    plt.title('K-means Clustering of Iris Dataset')
    plt.legend()
    plt.show()

kmeans_clustering()
