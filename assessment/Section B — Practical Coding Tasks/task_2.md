## Food Delivery Orders Data Cleaning Pipeline

```python
import numpy as np
import pandas as pd

orders = pd.DataFrame([
	[1001, "Aisha Khan", "Spice Route", "Indian", 32, 24.50, 4.5],
	[1002, "Ben Carter", "Green Bowl", "Healthy", 28, 18.75, 4.0],
	[1003, "Chloe Martin", "Pizza Corner", "Italian", 45, 31.20, 3.5],
	[1004, "Diego Silva", "Taco Town", "Mexican", 37, 22.90, 4.5],
	[1005, "Emma Wilson", "Noodle House", "Asian", 51, 27.40, 3.0],
	[1006, "Farah Ali", "Burger Lab", "American", 24, 16.80, 4.0],
	[1007, "George Lee", "Curry Leaf", "Indian", 40, 29.10, 4.5],
	[1008, "Hana Ito", "Sushi Daily", "Japanese", 35, 42.60, 5.0],
	[1009, "Ivan Petrov", "Pasta Place", "Italian", 48, 34.25, 3.5],
	[1010, "Julia Brown", "Falafel Stop", "Middle Eastern", 30, 19.95, 4.0],
	[1011, "Kofi Mensah", "Rice Bowl", "Asian", 43, 23.80, 4.5],
	[1012, "Laura Garcia", "Deli Express", "American", 26, 14.60, 3.0],
	[1013, "Min Park", "Seoul Kitchen", "Korean", 39, 36.50, 4.5],
	[1014, "Noah Smith", "Veggie Garden", "Healthy", 33, 21.75, 4.0],
	[1015, "Olivia Jones", "Taco Town", "Mexican", 55, 28.30, 2.5],
	[1016, "Priya Shah", "Spice Route", "Indian", 31, 26.90, 4.5],
	[1017, "Quinn Davis", "Pizza Corner", "Italian", 46, 30.10, 3.5],
	[1018, "Ravi Patel", "Burger Lab", "American", 22, 17.40, 4.0],
	[1019, "Sara Ahmed", "Sushi Daily", "Japanese", 38, 45.20, 5.0],
	[1020, "Tom Baker", "Noodle House", "Asian", 49, 150.00, 3.0],
], columns=[
	"order_id",
	"customer_name",
	"restaurant_name",
	"category",
	"delivery_time_mins",
	"order_value",
	"rating",
])

# Introduce missing values across categorical and numeric columns.
orders.loc[2, "customer_name"] = np.nan
orders.loc[7, "category"] = np.nan
orders.loc[4, "delivery_time_mins"] = np.nan
orders.loc[11, "order_value"] = np.nan
orders.loc[13, "rating"] = np.nan

# Add three complete duplicate rows.
duplicate_rows = orders.iloc[[0, 5, 10]].copy()
orders = pd.concat([orders, duplicate_rows], ignore_index=True)

print("Null counts before filling:")
print(orders.isna().sum())

# Impute numeric columns with their medians.
orders["delivery_time_mins"] = orders["delivery_time_mins"].fillna(
	orders["delivery_time_mins"].median()
)
orders["order_value"] = orders["order_value"].fillna(
	orders["order_value"].median()
)

# Impute rating with its mean rounded to one decimal place.
rating_mean = round(orders["rating"].mean(), 1)
orders["rating"] = orders["rating"].fillna(rating_mean)

# Impute the categorical value with the most frequent category.
category_mode = orders["category"].mode().iloc[0]
orders["category"] = orders["category"].fillna(category_mode)

print("\nNull counts after filling:")
print(orders.isna().sum())

shape_before = orders.shape
orders = orders.drop_duplicates().reset_index(drop=True)
shape_after = orders.shape
print(f"\nShape before deduplication: {shape_before}")
print(f"Shape after deduplication: {shape_after}")

# Detect order-value outliers with the 1.5 x IQR rule.
q1 = orders["order_value"].quantile(0.25)
q3 = orders["order_value"].quantile(0.75)
iqr = q3 - q1
lower_fence = q1 - 1.5 * iqr
upper_fence = q3 + 1.5 * iqr

outlier_mask = (
	(orders["order_value"] < lower_fence)
	| (orders["order_value"] > upper_fence)
)

print("\nOrder-value outliers:")
print(orders.loc[outlier_mask])
print(f"Lower fence: {lower_fence:.2f}")
print(f"Upper fence: {upper_fence:.2f}")

# Cap high order values at the upper fence.
orders["order_value"] = orders["order_value"].clip(upper=upper_fence)

print("\nMaximum order value after capping:")
print(f"${orders['order_value'].max():.2f}")

# Confirm the requested setup and cleaning results.
assert shape_before == (23, 7)
assert shape_after == (20, 7)
assert orders.isna().sum().sum() == 0
```

The dataset starts with 20 distinct orders, five manually introduced missing values, and three appended duplicate rows, giving 23 rows before cleaning. The pipeline reports null counts before and after imputation, removes duplicates, identifies outliers using the lower and upper IQR fences, and caps high `order_value` values with `clip(upper=upper_fence)`.
