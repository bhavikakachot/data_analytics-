## Top-Rated Products

```sql
WITH top_rated_products AS (
	SELECT *
	FROM Products
	WHERE rating > 4.5
)
SELECT *
FROM top_rated_products;
```
