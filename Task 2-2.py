import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)
x_vals = np.random.rand(150)
y_vals = 4 * x_vals + np.random.normal(0, 0.3, 150)
plt.figure(figsize=(10, 6))
plt.scatter(x_vals, y_vals, alpha=0.7)
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Scatter Plot of X vs. Y')
plt.grid(True)
plt.show()
