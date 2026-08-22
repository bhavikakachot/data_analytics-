## Restaurants Rated Above the Overall Average

```sql
SELECT name
FROM restaurants
WHERE rating > (
	SELECT AVG(rating)
	FROM restaurants
)
ORDER BY rating DESC;
```
