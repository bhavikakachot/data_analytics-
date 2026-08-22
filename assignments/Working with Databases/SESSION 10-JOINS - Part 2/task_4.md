## Display Restaurants Without Duplicates

```sql
SELECT DISTINCT
	r.id,
	r.name
FROM Restaurants AS r
INNER JOIN Reviews AS rv
	ON r.id = rv.restaurant_id;
```

Duplicates occurred because one restaurant can have many reviews, producing one joined row for each review.
