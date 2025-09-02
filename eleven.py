from sklearn.linear_model import Perceptron

# Input data (features)
X = [[0, 0], [0, 1], [1, 0], [1, 1]]

# AND Gate Implementation
y_and = [0, 0, 0, 1]  
model_and = Perceptron()
model_and.fit(X, y_and)
print("AND Gate Prediction:", model_and.predict(X))

# OR Gate Implementation
y_or = [0, 1, 1, 1]  
model_or = Perceptron()
model_or.fit(X, y_or)
print("OR Gate Prediction:", model_or.predict(X))
