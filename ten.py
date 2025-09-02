import pandas as pd
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA


df = pd.read_csv("iris.csv")  


X = df.iloc[:, :-1].values    
y = df.iloc[:, -1].values      

# -------- PCA ----------
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
print("PCA Result:\n", X_pca[:5])

# ------- LDA -----------
lda = LDA(n_components=2)
X_lda = lda.fit_transform(X, y)
print("LDA Result:\n", X_lda[:5])
