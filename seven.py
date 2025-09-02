# KNN Classifier on Glass Dataset using Euclidean & Manhattan Distance

# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def knn_classifier():

    df = pd.read_csv("glass.csv")

   
    X = df.drop("Type", axis=1).values
    y = df["Type"].values

   
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    clf_euclidean = KNeighborsClassifier(n_neighbors=3, metric="euclidean")
    clf_euclidean.fit(X_train, y_train)
    y_pred_euclidean = clf_euclidean.predict(X_test)
    accuracy_euclidean = accuracy_score(y_test, y_pred_euclidean)
    print("Accuracy with Euclidean distance:", accuracy_euclidean)

    clf_manhattan = KNeighborsClassifier(n_neighbors=3, metric="manhattan")
    clf_manhattan.fit(X_train, y_train)
    y_pred_manhattan = clf_manhattan.predict(X_test)
    accuracy_manhattan = accuracy_score(y_test, y_pred_manhattan)
    print("Accuracy with Manhattan distance:", accuracy_manhattan)


knn_classifier()
