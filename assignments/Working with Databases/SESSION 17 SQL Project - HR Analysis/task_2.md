## Restaurant Count by Cuisine

```sql
SELECT
	cuisine,
	COUNT(*) AS restaurant_count
FROM Restaurant
GROUP BY cuisine
ORDER BY restaurant_count DESC;
```
