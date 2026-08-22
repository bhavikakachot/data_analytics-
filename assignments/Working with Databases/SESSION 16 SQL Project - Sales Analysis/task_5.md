## FoodOrders KPI Summary

```sql
SELECT
	'Average Order Amount' AS kpi_name,
	ROUND(AVG(order_amount), 2) AS kpi_value
FROM FoodOrders

UNION ALL

SELECT
	'Unique Customers' AS kpi_name,
	COUNT(DISTINCT customer_name) AS kpi_value
FROM FoodOrders;
```
