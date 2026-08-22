## Restaurant Ranking Within Each Cuisine

```sql
WITH restaurant_ratings AS (
	SELECT
		r.id,
		r.name,
		r.cuisine,
		AVG(rv.rating) AS average_rating
	FROM Restaurant AS r
	JOIN Review AS rv
		ON rv.restaurant_id = r.id
	GROUP BY r.id, r.name, r.cuisine
)
SELECT
	name,
	cuisine,
	ROUND(average_rating, 2) AS average_rating,
	DENSE_RANK() OVER (
		PARTITION BY cuisine
		ORDER BY average_rating DESC
	) AS cuisine_rank
FROM restaurant_ratings
ORDER BY cuisine, cuisine_rank;
```
