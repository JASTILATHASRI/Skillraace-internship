import pandas as pd
import numpy as np
date_range = pd.date_range(start='2025-01-01', end='2025-12-31', freq='D')
data_values = np.random.randn(len(date_range))
time_series_df = pd.DataFrame(data_values, index=date_range, columns=['Value'])
print(time_series_df.head())
