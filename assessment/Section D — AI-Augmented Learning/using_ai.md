## Step 1: Build with AI

### 1. Exact prompt given to the AI tool

> Write a Python program using `sqlite3`, Pandas, and Matplotlib. It should connect to a SQLite database containing an `orders` table with these columns: `order_id`, `restaurant_name`, `category`, `order_value`, `rating`, and `delivery_time_mins`. Query the top three restaurants by average customer rating, considering only restaurants with at least five orders. Load the SQL result into a Pandas DataFrame and add a `revenue_share_pct` column showing each restaurant's percentage of the total revenue across the three returned restaurants. Plot a horizontal bar chart ranked by average rating and display each restaurant's revenue share percentage as a label on its bar. Handle a missing database file and an empty query result with clear, user-friendly messages instead of crashing. Return the complete code and include labelled axes.

### 2. AI's original code

```python
import sqlite3

import matplotlib.pyplot as plt
import pandas as pd

connection = sqlite3.connect("food_delivery.db")

query = """
	SELECT restaurant_name,
		   AVG(rating) AS average_rating,
		   SUM(order_value) AS total_revenue,
		   COUNT(*) AS order_count
	FROM orders
	ORDER BY average_rating DESC
	HAVING COUNT(*) >= 5
	GROUP BY restaurant_name
	LIMIT 3
"""

results = pd.read_sql_query(query, connection)
connection.close()

total_revenue = results["total_revenue"].sum()
results["revenue_share_pct"] = (
	results["total_revenue"] / total_revenue * 100
)

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(results["restaurant_name"], results["average_rating"])
ax.set_title("Top 3 Restaurants by Average Rating")

for bar, share in zip(bars, results["revenue_share_pct"]):
	ax.text(
		bar.get_width(),
		bar.get_y() + bar.get_height() / 2,
		f"{share:.1f}%",
		va="center",
	)

plt.show()
```

## Step 2: Test and Debug Without AI

### Corrected version

```python
from pathlib import Path
import sqlite3

import matplotlib.pyplot as plt
import pandas as pd


DATABASE_PATH = Path("food_delivery.db")


def build_report():
	if not DATABASE_PATH.is_file():
		print(f"Database not found: {DATABASE_PATH.resolve()}")
		print("Create food_delivery.db with an orders table before running this report.")
		return None

	query = """
		SELECT
			restaurant_name,
			AVG(rating) AS average_rating,
			SUM(order_value) AS total_revenue,
			COUNT(order_id) AS order_count
		FROM orders
		GROUP BY restaurant_name
		HAVING COUNT(order_id) >= 5
		ORDER BY average_rating DESC
		LIMIT 3
	"""

	try:
		with sqlite3.connect(DATABASE_PATH) as connection:
			results = pd.read_sql_query(query, connection)
	except sqlite3.Error as error:
		print(f"Could not read the database: {error}")
		return None

	if results.empty:
		print("No restaurants have at least five orders, so there is no report to plot.")
		return None

	total_revenue = results["total_revenue"].sum()
	if total_revenue <= 0:
		print("The top restaurants have no positive revenue, so revenue share cannot be calculated.")
		return None

	results["revenue_share_pct"] = (
		results["total_revenue"] / total_revenue * 100.0
	)
	results = results.sort_values("average_rating", ascending=True)

	figure, axis = plt.subplots(figsize=(10, 6))
	bars = axis.barh(
		results["restaurant_name"],
		results["average_rating"],
		color="steelblue",
	)
	axis.bar_label(
		bars,
		labels=[f"{share:.1f}% revenue" for share in results["revenue_share_pct"]],
		padding=4,
	)
	axis.set_title("Top 3 Restaurants by Average Customer Rating")
	axis.set_xlabel("Average customer rating")
	axis.set_ylabel("Restaurant")
	axis.set_xlim(0, max(5, results["average_rating"].max() * 1.2))
	figure.tight_layout()
	plt.show()
	return results


report = build_report()
if report is not None:
	print("Top restaurants:")
	print(report.to_string(index=False))
```

### 3. What I changed and why

The AI version placed `HAVING` before `GROUP BY`, which is invalid SQL; I moved `GROUP BY` before `HAVING`. I added a file-existence check, database error handling, and an empty-DataFrame check so missing or insufficient data produces a clear message instead of a crash. I used floating-point percentage arithmetic and guarded against zero revenue. Finally, I added explicit x- and y-axis labels and used `bar_label` for readable revenue-share annotations.
