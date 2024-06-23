import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(123)
data_values = {
    'Group': np.random.choice(['X', 'Y', 'Z', 'W', 'V'], 150),
    'Values': np.random.randn(150)
}
df_new = pd.DataFrame(data_values)
plt.figure(figsize=(12, 6))
sns.boxplot(x='Group', y='Values', data=df_new)
plt.xlabel('Groups')
plt.ylabel('Values')
plt.title('Modified Box Plot of Values by Group')
plt.grid(True)
plt.show()
