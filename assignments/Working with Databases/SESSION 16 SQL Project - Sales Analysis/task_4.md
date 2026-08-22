## Restaurant Performance Report

```sql
SELECT
	restaurant_name,
	COUNT(*) AS number_of_orders,
	SUM(order_amount) AS total_order_amount
FROM FoodOrders
GROUP BY restaurant_name
ORDER BY total_order_amount DESC;
```
