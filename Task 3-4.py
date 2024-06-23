import pandas as pd
original_period = pd.Period('2025-01', freq='M')
future_period = original_period + 3
print("Future Period:", future_period)
past_period = original_period - 2
print("Past Period:", past_period)
start_period = '2025-01'
end_period = '2025-12'
periods_range = pd.period_range(start=start_period, end=end_period, freq='M')
print("Periods Range:", periods_range)
