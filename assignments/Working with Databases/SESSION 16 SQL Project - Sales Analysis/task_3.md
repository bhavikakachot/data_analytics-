## Top 3 Customers by Total Spending

```sql
SELECT
	customer_name,
	SUM(order_amount) AS total_spent
FROM FoodOrders
GROUP BY customer_name
ORDER BY total_spent DESC
LIMIT 3;
```
