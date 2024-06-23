import pandas as pd
import matplotlib.pyplot as plt
data_values = {
    'Group X Data': [10, 20, 30, 40, 50],
    'Group Y Data': [15, 25, 35, 45, 55],
    'Group Z Data': [20, 30, 40, 50, 60]
}
index_items = ['Product 1', 'Product 2', 'Product 3', 'Product 4', 'Product 5']
df_plot = pd.DataFrame(data_values, index=index_items)
plot1 = df_plot.plot(kind='bar', figsize=(10, 6))
plot1.set_xlabel('Products')
plot1.set_ylabel('Values')
plot1.set_title('Modified Side-by-Side Bar Plot')
plt.xticks(rotation=0)
plt.show()
plot2 = df_plot.plot(kind='bar', stacked=True, figsize=(10, 6))
plot2.set_xlabel('Products')
plot2.set_ylabel('Values')
plot2.set_title('Modified Stacked Bar Plot')
plt.xticks(rotation=0)
plt.show()
