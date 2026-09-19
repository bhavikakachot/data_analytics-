## Daily Order Analysis with NumPy

```python
import numpy as np

# Use a fixed seed so the generated data is reproducible.
np.random.seed(42)

daily_orders = np.random.randint(100, 801, size=30)
daily_revenue = np.random.uniform(5000, 50000, size=30)

total_orders = np.sum(daily_orders)
total_revenue = np.sum(daily_revenue)
mean_orders = np.mean(daily_orders)
std_orders = np.std(daily_orders)
highest_revenue_index = np.argmax(daily_revenue)

peak_threshold = mean_orders + std_orders
peak_day_mask = daily_orders > peak_threshold
peak_day_orders = daily_orders[peak_day_mask]
peak_day_revenue = daily_revenue[peak_day_mask]

weekly_orders = daily_orders.reshape(5, 6)
orders_per_week = np.sum(weekly_orders, axis=1)

print(f"Total orders: {total_orders}")
print(f"Total revenue: ${total_revenue:,.2f}")
print(f"Mean daily orders: {mean_orders:.2f}")
print(f"Standard deviation of daily orders: {std_orders:.2f}")
print(f"Highest revenue day index (zero-based): {highest_revenue_index}")
print(f"Peak-day threshold: {peak_threshold:.2f}")
print(f"Number of peak days: {peak_day_orders.size}")
print(f"Combined peak-day revenue: ${np.sum(peak_day_revenue):,.2f}")
print(f"Orders by weekly block: {orders_per_week}")
```

`peak_day_mask` is a Boolean array with one value per day. Boolean indexing uses `True` values to extract the order counts and matching revenue values for days whose order count exceeds the mean by more than one standard deviation. `reshape(5, 6)` groups the 30 daily values into five six-day blocks, and `np.sum(..., axis=1)` returns one total for each row.
