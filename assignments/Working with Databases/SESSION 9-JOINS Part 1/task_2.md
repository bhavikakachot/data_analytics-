## Display Dishes with Restaurant Information

```sql
SELECT
	d.dish_name,
	r.name AS restaurant_name,
	r.city
FROM dishes AS d
INNER JOIN restaurants AS r
	ON d.restaurant_id = r.id;
```
