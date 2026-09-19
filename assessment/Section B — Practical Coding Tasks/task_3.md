## Food Delivery Visualisation Dashboard

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fresh reproducible simulation with the same columns as the cleaned dataset.
rng = np.random.default_rng(42)
restaurants = np.array([
	"Spice Route",
	"Green Bowl",
	"Pizza Corner",
	"Taco Town",
	"Burger Lab",
	"Sushi Daily",
])
categories_by_restaurant = {
	"Spice Route": "Indian",
	"Green Bowl": "Healthy",
	"Pizza Corner": "Italian",
	"Taco Town": "Mexican",
	"Burger Lab": "American",
	"Sushi Daily": "Japanese",
}

restaurant_values = rng.choice(restaurants, size=30)
orders = pd.DataFrame({
	"order_id": [f"ORD-{number}" for number in range(1001, 1031)],
	"customer_name": [f"Customer {number}" for number in range(1, 31)],
	"restaurant_name": restaurant_values,
	"category": [categories_by_restaurant[name] for name in restaurant_values],
	"delivery_time_mins": rng.integers(20, 65, size=30),
	"order_value": np.round(rng.uniform(12, 75, size=30), 2),
	"rating": np.round(rng.uniform(2.5, 5.0, size=30), 1),
})

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Top-left: order count by restaurant category.
sns.countplot(data=orders, x="category", ax=axes[0, 0])
axes[0, 0].set_title("Order Count by Restaurant Category")
axes[0, 0].set_xlabel("Restaurant category")
axes[0, 0].set_ylabel("Number of orders")
axes[0, 0].tick_params(axis="x", rotation=30)

# Top-right: delivery-time distribution by category.
sns.boxplot(data=orders, x="category", y="delivery_time_mins", ax=axes[0, 1])
axes[0, 1].set_title("Delivery Time Distribution by Category")
axes[0, 1].set_xlabel("Restaurant category")
axes[0, 1].set_ylabel("Delivery time (minutes)")
axes[0, 1].tick_params(axis="x", rotation=30)

# Bottom-left: average order value by restaurant.
average_value = (
	orders.groupby("restaurant_name")["order_value"]
	.mean()
	.sort_values()
)
axes[1, 0].barh(average_value.index, average_value.values, color="teal")
axes[1, 0].set_title("Average Order Value by Restaurant")
axes[1, 0].set_xlabel("Average order value")
axes[1, 0].set_ylabel("Restaurant")

# Bottom-right: correlations among all numeric measures.
numeric_correlation = orders.select_dtypes(include="number").corr()
sns.heatmap(numeric_correlation, annot=True, cmap="YlGnBu", fmt=".2f", ax=axes[1, 1])
axes[1, 1].set_title("Correlation Matrix of Numeric Order Measures")
axes[1, 1].set_xlabel("Numeric measure")
axes[1, 1].set_ylabel("Numeric measure")

fig.suptitle("Food Delivery Operations Dashboard", fontsize=16)
plt.tight_layout()
plt.savefig("food_delivery_dashboard.png", dpi=150, bbox_inches="tight")
print("Dashboard saved as food_delivery_dashboard.png")
plt.show()
```

The dashboard uses one shared figure with four focused views: category volume, delivery-time spread, restaurant-level order value, and numeric correlations. `plt.tight_layout()` is applied before saving so subplot labels do not overlap.
