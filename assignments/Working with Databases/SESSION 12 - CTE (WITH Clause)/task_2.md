## Restaurants in Ahmedabad With Low Delivery Charges

### Using a Subquery

```sql
SELECT *
FROM (
	SELECT *
	FROM Restaurants
	WHERE city = 'Ahmedabad'
		AND delivery_charges < 50
) AS affordable_ahmedabad_restaurants;
```

### Using a CTE

```sql
WITH affordable_ahmedabad_restaurants AS (
	SELECT *
	FROM Restaurants
	WHERE city = 'Ahmedabad'
		AND delivery_charges < 50
)
SELECT *
FROM affordable_ahmedabad_restaurants;
```

### Readability Comparison

Both queries return the same results. The CTE version is cleaner because it gives the filtered result a meaningful name before selecting from it. This makes the query easier to read and extend, especially when the filtered data is reused or additional CTEs are added.
