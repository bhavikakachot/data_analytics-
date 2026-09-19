## SQL + Python Restaurant Performance Report

```python
import sqlite3

import pandas as pd

database_path = "food_delivery.db"

restaurants = [
	(1, "Spice Route", "Indian", "London"),
	(2, "Green Bowl", "Healthy", "London"),
	(3, "Pizza Corner", "Italian", "Manchester"),
	(4, "Taco Town", "Mexican", "Birmingham"),
	(5, "Noodle House", "Asian", "Leeds"),
	(6, "Burger Lab", "American", "Manchester"),
	(7, "Sushi Daily", "Japanese", "London"),
	(8, "Falafel Stop", "Middle Eastern", "Bristol"),
]

orders = [
	(1, 1, 24.50, 32, 4.5),
	(2, 1, 31.20, 38, 4.0),
	(3, 1, 28.75, 35, 4.5),
	(4, 2, 18.75, 28, 4.0),
	(5, 2, 22.40, 31, 4.5),
	(6, 2, 16.80, 26, 3.5),
	(7, 3, 31.20, 45, 3.5),
	(8, 3, 34.25, 48, 4.0),
	(9, 3, 29.90, 42, 3.5),
	(10, 4, 22.90, 37, 4.5),
	(11, 4, 28.30, 55, 3.0),
	(12, 4, 25.60, 41, 4.0),
	(13, 5, 27.40, 51, 3.0),
	(14, 5, 23.80, 43, 4.5),
	(15, 5, 25.65, 49, 3.5),
	(16, 6, 16.80, 24, 4.0),
	(17, 6, 21.40, 29, 4.5),
	(18, 6, 19.75, 27, 4.0),
	(19, 7, 42.60, 35, 5.0),
	(20, 7, 45.20, 38, 5.0),
	(21, 7, 39.80, 34, 4.5),
	(22, 8, 19.95, 30, 4.0),
	(23, 8, 21.50, 33, 3.5),
	(24, 1, 26.40, 36, 4.0),
	(25, 3, 37.10, 52, 3.0),
]

with sqlite3.connect(database_path) as connection:
	connection.execute("PRAGMA foreign_keys = ON")

	connection.executescript(
		"""
		DROP TABLE IF EXISTS orders;
		DROP TABLE IF EXISTS restaurants;

		CREATE TABLE restaurants (
			restaurant_id INTEGER PRIMARY KEY,
			name TEXT NOT NULL,
			category TEXT NOT NULL,
			city TEXT NOT NULL
		);

		CREATE TABLE orders (
			order_id INTEGER PRIMARY KEY,
			restaurant_id INTEGER NOT NULL,
			order_value REAL NOT NULL,
			delivery_time_mins REAL NOT NULL,
			rating REAL NOT NULL,
			FOREIGN KEY (restaurant_id) REFERENCES restaurants (restaurant_id)
		);
		"""
	)

	connection.executemany(
		"""
		INSERT INTO restaurants (restaurant_id, name, category, city)
		VALUES (?, ?, ?, ?)
		""",
		restaurants,
	)
	connection.executemany(
		"""
		INSERT INTO orders
			(order_id, restaurant_id, order_value, delivery_time_mins, rating)
		VALUES (?, ?, ?, ?, ?)
		""",
		orders,
	)

	performance_query = """
		SELECT
			r.restaurant_id,
			r.name,
			r.category,
			r.city,
			COUNT(o.order_id) AS total_orders,
			COALESCE(SUM(o.order_value), 0) AS total_revenue,
			ROUND(AVG(o.rating), 2) AS avg_rating
		FROM restaurants AS r
		LEFT JOIN orders AS o
			ON r.restaurant_id = o.restaurant_id
		GROUP BY r.restaurant_id, r.name, r.category, r.city
		ORDER BY total_revenue DESC
	"""

	report = pd.read_sql_query(performance_query, connection)

report["revenue_rank"] = (
	report["total_revenue"]
	.rank(ascending=False, method="min")
	.astype(int)
)
report = report.sort_values("revenue_rank", ascending=True).reset_index(drop=True)

print("Full restaurant performance report:")
print(report.to_string(index=False))

print("\nTop 5 restaurants by total revenue:")
top_five = report.head(5)
print(top_five.to_string(index=False))

report.to_csv("restaurant_performance_report.csv", index=False)
print("\nReport exported to restaurant_performance_report.csv")
```

The `LEFT JOIN` preserves all eight restaurants in the report, while `COUNT(o.order_id)` correctly returns zero for a restaurant without orders. `pd.read_sql_query()` converts the grouped SQL result into a DataFrame before the revenue ranking and CSV export are applied.
