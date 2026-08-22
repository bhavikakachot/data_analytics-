## Import Food Delivery Orders from CSV

This script expects a file named `food_delivery_orders.csv` with the columns
`order_id`, `restaurant_name`, `customer_name`, `order_amount`, and `order_date`.

```python
import sqlite3

import pandas as pd

csv_file = 'food_delivery_orders.csv'
required_columns = {
	'order_id',
	'restaurant_name',
	'customer_name',
	'order_amount',
	'order_date'
}

orders_df = pd.read_csv(csv_file)
missing_columns = required_columns - set(orders_df.columns)

if missing_columns:
	raise ValueError(
		f'Missing required columns: {sorted(missing_columns)}'
	)

with sqlite3.connect('foodie.db') as connection:
	connection.execute('DROP TABLE IF EXISTS FoodOrders')
	connection.execute('''
		CREATE TABLE FoodOrders (
			order_id INTEGER PRIMARY KEY,
			restaurant_name TEXT NOT NULL,
			customer_name TEXT NOT NULL,
			order_amount REAL NOT NULL,
			order_date DATE NOT NULL
		)
	''')

	orders_df.to_sql(
		'FoodOrders',
		connection,
		if_exists='append',
		index=False
	)

print(f'{len(orders_df)} orders imported into FoodOrders.')
```
