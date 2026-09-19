## Food Delivery Analytics Console Application

```python
from pathlib import Path
import sqlite3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


DATABASE_PATH = "food_delivery.db"
EXPORT_PATH = "food_delivery_report.xlsx"


def create_simulated_orders():
	rng = np.random.default_rng(42)
	restaurant_catalog = [
		("Spice Route", "Indian", "London"),
		("Green Bowl", "Healthy", "London"),
		("Pizza Corner", "Italian", "Manchester"),
		("Taco Town", "Mexican", "Birmingham"),
		("Noodle House", "Asian", "Leeds"),
		("Burger Lab", "American", "Manchester"),
		("Sushi Daily", "Japanese", "London"),
		("Falafel Stop", "Middle Eastern", "Bristol"),
	]

	restaurant_indexes = rng.integers(0, len(restaurant_catalog), size=30)
	selected_restaurants = [restaurant_catalog[index] for index in restaurant_indexes]

	orders = pd.DataFrame({
		"order_id": np.arange(1001, 1031),
		"customer_name": [f"Customer {number}" for number in range(1, 31)],
		"restaurant_name": [item[0] for item in selected_restaurants],
		"category": [item[1] for item in selected_restaurants],
		"city": [item[2] for item in selected_restaurants],
		"delivery_time_mins": rng.integers(20, 65, size=30).astype(float),
		"order_value": np.round(rng.uniform(12, 75, size=30), 2),
		"rating": np.round(rng.uniform(2.5, 5.0, size=30), 1),
	})

	orders.loc[2, "customer_name"] = np.nan
	orders.loc[7, "category"] = np.nan
	orders.loc[4, "city"] = np.nan
	orders.loc[11, "delivery_time_mins"] = np.nan
	orders.loc[13, "order_value"] = np.nan
	orders.loc[15, "rating"] = np.nan
	orders.loc[19, "order_value"] = 150.00

	duplicate_rows = orders.iloc[[0, 5, 10]].copy()
	return pd.concat([orders, duplicate_rows], ignore_index=True)


def quality_summary(dataframe):
	return pd.DataFrame({
		"rows": [len(dataframe)],
		"columns": [len(dataframe.columns)],
		"missing_cells": [int(dataframe.isna().sum().sum())],
		"duplicate_rows": [int(dataframe.duplicated().sum())],
	})


def print_quality_summary(label, dataframe):
	print(f"\n{label} data quality summary:")
	print(quality_summary(dataframe).to_string(index=False))


def load_and_clean_data():
	orders = create_simulated_orders()
	print_quality_summary("Before cleaning", orders)

	orders["delivery_time_mins"] = orders["delivery_time_mins"].fillna(
		orders["delivery_time_mins"].median()
	)
	orders["order_value"] = orders["order_value"].fillna(
		orders["order_value"].median()
	)
	orders["rating"] = orders["rating"].fillna(
		round(orders["rating"].mean(), 1)
	)

	categorical_columns = [
		"customer_name",
		"restaurant_name",
		"category",
		"city",
	]
	for column in categorical_columns:
		orders[column] = orders[column].fillna(orders[column].mode().iloc[0])

	orders = orders.drop_duplicates().reset_index(drop=True)

	q1 = orders["order_value"].quantile(0.25)
	q3 = orders["order_value"].quantile(0.75)
	iqr = q3 - q1
	lower_fence = q1 - 1.5 * iqr
	upper_fence = q3 + 1.5 * iqr
	outlier_mask = (
		(orders["order_value"] < lower_fence)
		| (orders["order_value"] > upper_fence)
	)

	print("\nOrder-value outliers before capping:")
	print(orders.loc[outlier_mask].to_string(index=False))
	print(f"Lower fence: {lower_fence:.2f}")
	print(f"Upper fence: {upper_fence:.2f}")

	orders["order_value"] = orders["order_value"].clip(
		lower=lower_fence,
		upper=upper_fence,
	)
	print_quality_summary("After cleaning", orders)
	return orders


def create_database(cleaned_orders):
	restaurant_table = (
		cleaned_orders[["restaurant_name", "category", "city"]]
		.drop_duplicates()
		.sort_values("restaurant_name")
		.reset_index(drop=True)
	)
	restaurant_table.insert(
		0,
		"restaurant_id",
		np.arange(1, len(restaurant_table) + 1),
	)

	order_table = cleaned_orders.merge(
		restaurant_table,
		on=["restaurant_name", "category", "city"],
		how="left",
	)

	with sqlite3.connect(DATABASE_PATH) as connection:
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
			restaurant_table[
				["restaurant_id", "restaurant_name", "category", "city"]
			].itertuples(index=False, name=None),
		)
		connection.executemany(
			"""
			INSERT INTO orders
				(order_id, restaurant_id, order_value, delivery_time_mins, rating)
			VALUES (?, ?, ?, ?, ?)
			""",
			order_table[
				[
					"order_id",
					"restaurant_id",
					"order_value",
					"delivery_time_mins",
					"rating",
				]
			].itertuples(index=False, name=None),
		)


def run_sql_analysis(cleaned_orders):
	create_database(cleaned_orders)
	group_query = """
		SELECT
			r.category,
			COUNT(o.order_id) AS total_orders,
			ROUND(SUM(o.order_value), 2) AS total_revenue,
			ROUND(AVG(o.rating), 2) AS average_rating
		FROM restaurants AS r
		LEFT JOIN orders AS o
			ON r.restaurant_id = o.restaurant_id
		GROUP BY r.category
		ORDER BY total_revenue DESC
	"""
	join_query = """
		SELECT
			o.order_id,
			r.name AS restaurant_name,
			r.category,
			r.city,
			o.order_value,
			o.delivery_time_mins,
			o.rating
		FROM orders AS o
		JOIN restaurants AS r
			ON o.restaurant_id = r.restaurant_id
		ORDER BY o.order_id
	"""

	with sqlite3.connect(DATABASE_PATH) as connection:
		category_summary = pd.read_sql_query(group_query, connection)
		order_details = pd.read_sql_query(join_query, connection)

	print("\nSQL aggregate analysis by category:")
	print(category_summary.to_string(index=False))
	print("\nSQL JOIN analysis - order details:")
	print(order_details.to_string(index=False))
	return category_summary, order_details


def view_charts(cleaned_orders):
	figure, axes = plt.subplots(1, 2, figsize=(14, 5))
	sns.countplot(data=cleaned_orders, x="category", ax=axes[0])
	axes[0].set_title("Orders by Restaurant Category")
	axes[0].set_xlabel("Category")
	axes[0].set_ylabel("Order count")
	axes[0].tick_params(axis="x", rotation=30)

	city_delivery = (
		cleaned_orders.groupby("city", as_index=False)["delivery_time_mins"]
		.mean()
	)
	sns.barplot(
		data=city_delivery,
		x="city",
		y="delivery_time_mins",
		ax=axes[1],
		errorbar=None,
	)
	axes[1].set_title("Average Delivery Time by City")
	axes[1].set_xlabel("City")
	axes[1].set_ylabel("Average delivery time (minutes)")
	axes[1].tick_params(axis="x", rotation=30)

	figure.suptitle("Food Delivery Analytics", fontsize=16)
	figure.tight_layout()
	plt.show()


def export_report(cleaned_orders, category_summary, order_details):
	with pd.ExcelWriter(EXPORT_PATH) as writer:
		cleaned_orders.to_excel(writer, sheet_name="Cleaned Orders", index=False)
		category_summary.to_excel(writer, sheet_name="SQL Summary", index=False)
		order_details.to_excel(writer, sheet_name="SQL Join Details", index=False)

	print(f"Report exported to: {Path(EXPORT_PATH).resolve()}")


def print_menu():
	print(
		"\nFood Delivery Analytics\n"
		"1. Load & Clean Data\n"
		"2. Run SQL Analysis\n"
		"3. View Charts\n"
		"4. Export Report\n"
		"0. Exit"
	)


def main():
	cleaned_orders = None
	category_summary = None
	order_details = None

	while True:
		print_menu()
		choice = input("Select an option: ").strip()

		if choice == "1":
			cleaned_orders = load_and_clean_data()
			category_summary = None
			order_details = None
		elif choice == "2":
			if cleaned_orders is None:
				print("Load and clean the data first using option 1.")
				continue
			category_summary, order_details = run_sql_analysis(cleaned_orders)
		elif choice == "3":
			if cleaned_orders is None:
				print("Load and clean the data first using option 1.")
				continue
			view_charts(cleaned_orders)
		elif choice == "4":
			if cleaned_orders is None:
				print("Load and clean the data first using option 1.")
				continue
			if category_summary is None or order_details is None:
				category_summary, order_details = run_sql_analysis(cleaned_orders)
			export_report(cleaned_orders, category_summary, order_details)
		elif choice == "0":
			print("Goodbye.")
			break
		else:
			print("Invalid option. Choose 0, 1, 2, 3, or 4.")


if __name__ == "__main__":
	main()
```

The application keeps the cleaned DataFrame and SQL result tables in memory so the menu options can be run in sequence without repeating work. Option 4 automatically runs the SQL analysis if it has not already been selected, then writes the cleaned data, aggregate results, and join results to separate sheets in `food_delivery_report.xlsx`.
