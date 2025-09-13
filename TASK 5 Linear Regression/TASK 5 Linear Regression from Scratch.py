import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

housing = fetch_california_housing()
X, y = housing.data, housing.target

X = X[:, [0]]  


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

class ManualLinearRegression:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.w = None
        self.b = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.w = np.zeros(n_features)   
        self.b = 0                      

        
        for _ in range(self.n_iterations):
            
            y_pred = np.dot(X, self.w) + self.b

            
            dw = (1/n_samples) * np.dot(X.T, (y_pred - y))
            db = (1/n_samples) * np.sum(y_pred - y)

            
            self.w -= self.learning_rate * dw
            self.b -= self.learning_rate * db

    def predict(self, X):
        return np.dot(X, self.w) + self.b

manual_lr = ManualLinearRegression(learning_rate=0.1, n_iterations=1000)
manual_lr.fit(X_train, y_train)

y_pred_manual = manual_lr.predict(X_test)

mse = mean_squared_error(y_test, y_pred_manual)
mae = mean_absolute_error(y_test, y_pred_manual)
r2 = r2_score(y_test, y_pred_manual)

print("Manual Linear Regression Performance:")
print(f"MSE: {mse:.4f}")
print(f"MAE: {mae:.4f}")
print(f"R² : {r2:.4f}")

plt.figure(figsize=(10,6))
plt.scatter(X_test, y_test, color="blue", alpha=0.5, label="Data Points")
plt.plot(X_test, y_pred_manual, color="red", linewidth=2, label="Manual Model")
plt.xlabel("Median Income (scaled)")
plt.ylabel("House Value")
plt.title("Linear Regression (Manual Implementation)")
plt.legend()
plt.show()

