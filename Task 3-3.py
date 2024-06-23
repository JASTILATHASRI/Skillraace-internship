import pandas as pd
start_date_utc = '2025-01-01'
end_date_utc = '2025-01-05'
date_index_utc = pd.date_range(start=start_date_utc, end=end_date_utc, freq='D', tz='UTC')
print(date_index_utc)
start_date_localize = '2025-01-01'
end_date_localize = '2025-01-05'
date_index_localize = pd.date_range(start=start_date_localize, end=end_date_localize, freq='D')
date_index_localize = date_index_localize.tz_localize('America/New_York')
print(date_index_localize)
date_index_convert = date_index_localize.tz_convert('Europe/London')
print(date_index_convert)
date_index1_combined = pd.date_range(start=start_date_utc, periods=3, freq='D', tz='UTC')
date_index2_combined = pd.date_range(start=start_date_utc, periods=3, freq='D', tz='America/New_York')
combined_index = date_index1_combined.union(date_index2_combined)
print(combined_index)
