import pandas as pd
import numpy as np
data_new = {
    'X': [10, 20, np.nan, 40, 50, np.nan, 70],
    'Y': [np.nan, 20, 30, 40, np.nan, 60, 70],
    'Z': ['alpha', 'beta', 'gamma', np.nan, 'delta', 'epsilon', 'zeta'],
    'W': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
}
df_new = pd.DataFrame(data_new)
print("Original DataFrame:")
print(df_new)

missing_data_new = df_new.isna()
print("\nMissing Data in DataFrame:")
print(missing_data_new)

df_new_dropna_rows = df_new.dropna()
print("\nDataFrame after dropping rows with any missing data:")
print(df_new_dropna_rows)
df_new_dropna_cols = df_new.dropna(axis=1)
print("\nDataFrame after dropping columns with any missing data:")
print(df_new_dropna_cols)
df_new_fillna = df_new.fillna(value={'X': df_new['X'].mean(), 'Y': df_new['Y'].mean(), 'Z': 'missing', 'W': 0})
print("\nDataFrame after filling missing data:")
print(df_new_fillna)
df_new_with_duplicates = df_new.append(df_new.iloc[2], ignore_index=True)
print("\nDataFrame with Duplicates:")
print(df_new_with_duplicates)
duplicates_new = df_new_with_duplicates.duplicated()
print("\nDuplicates in DataFrame:")
print(duplicates_new)
df_new_no_duplicates = df_new_with_duplicates.drop_duplicates()
print("\nDataFrame after removing duplicates:")
print(df_new_no_duplicates)
