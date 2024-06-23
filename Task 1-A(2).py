import pandas as pd
data_list = [100, 200, 300, 400, 500, 600]
idx = pd.MultiIndex.from_tuples([('P', 1), ('P', 2), ('Q', 1), ('Q', 2), ('R', 1), ('R', 2)])
new_series = pd.Series(data_list, index=idx)

print("Series with MultiIndex:")
print(new_series)
subset_P = new_series.loc['P']
print("\nSubset P:")
print(subset_P)
subset_P_inner_2 = new_series.loc[('P', 2)]
print("\nSubset P, Inner 2:")
print(subset_P_inner_2)
subset_Q = new_series.loc['Q']
print("\nSubset Q:")
print(subset_Q)
subset_R_inner_1 = new_series.loc[('R', 1)]
print("\nSubset R, Inner 1:")
print(subset_R_inner_1)
subset_Q_xs = new_series.xs('Q')
print("\nSubset Q using xs:")
print(subset_Q_xs)
subset_inner_2_xs = new_series.xs(2, level=1)
print("\nSubset Inner Level 2 using xs:")
print(subset_inner_2_xs)
