import pandas as pd
start_date = '2025-01-01'
end_date_range = '2025-12-31'
date_index_range = pd.date_range(start=start_date, end=end_date_range)
print(date_index_range)
start_date_periods = '2025-01-01'
periods = 365  
date_index_periods = pd.date_range(start=start_date_periods, periods=periods)
print(date_index_periods)
end_date_periods = '2025-12-31'
periods_end = 365
date_index_end = pd.date_range(end=end_date_periods, periods=periods_end)
print(date_index_end)
start_date_freq = '2025-01-01'
end_date_freq = '2025-12-31'
date_index_freq = pd.date_range(start=start_date_freq, end=end_date_freq, freq='D')  # 'D' generates dates on a daily basis
print(date_index_freq)
