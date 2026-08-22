## Display All Dishes with Restaurant Names

```sql
SELECT
	d.dish_name,
	d.restaurant_id,
	r.name AS restaurant_name
FROM restaurants AS r
RIGHT JOIN dishes AS d
	ON r.id = d.restaurant_id;
```

If a dish has no matching restaurant, it still appears with `NULL` for `restaurant_name`.
