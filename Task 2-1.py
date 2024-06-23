import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
random_values = np.random.normal(loc=10, scale=3, size=1500)
plt.figure(figsize=(10, 6))
plt.hist(random_values, bins=40, edgecolor='black', alpha=0.6)
plt.xlabel('Random Values')
plt.ylabel('Frequency')
plt.title('Histogram of Random Value Frequency')
plt.grid(True)
plt.show()
plt.figure(figsize=(10, 6))
sns.kdeplot(random_values, fill=True)
plt.xlabel('Random Values')
plt.ylabel('Density')
plt.title('Density Plot of Random Continuous Probability Distribution')
plt.grid(True)
plt.show()
