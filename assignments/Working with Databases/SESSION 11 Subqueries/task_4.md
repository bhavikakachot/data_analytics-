## Find Sellers in Every Category

Assuming `Products` contains `seller_id` and `category_id` columns:

```sql
SELECT s.name
FROM Sellers AS s
WHERE NOT EXISTS (
	SELECT 1
	FROM Categories AS c
	WHERE NOT EXISTS (
		SELECT 1
		FROM Products AS p
		WHERE p.seller_id = s.id
			AND p.category_id = c.id
	)
);
```

The nested subqueries return a seller only when no category is missing from that seller's products.
