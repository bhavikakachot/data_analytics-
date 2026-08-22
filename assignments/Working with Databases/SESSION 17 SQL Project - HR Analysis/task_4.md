## Average Review Rating by Restaurant

```sql
SELECT
	r.name,
	r.cuisine,
	ROUND(AVG(rv.rating), 2) AS average_review_rating
FROM Restaurant AS r
JOIN Review AS rv
	ON rv.restaurant_id = r.id
GROUP BY r.id, r.name, r.cuisine
ORDER BY average_review_rating DESC;
```
