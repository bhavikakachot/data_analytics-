## Find Highest and Lowest Order Amounts

```sql
SELECT
	MAX(total_amount) AS highest_order_amount,
	MIN(total_amount) AS lowest_order_amount
FROM Orders;
```
