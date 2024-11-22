import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

np.random.seed(42)
x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)

model = LinearRegression()
model.fit(x, y)
X_new = np.array([[0], [2]])
y_pred = model.predict(X_new)
plt.scatter(x, y, label='Original data')
plt.plot(X_new, y_pred, 'r--', label='Regression line')
plt.xlabel('x')
plt.plot('y')
plt.legend()
plt.show()

print("Intercept(beta_0:", model.intercept_[0])
print('slope(beta_1):', model.coef_[0][0])
