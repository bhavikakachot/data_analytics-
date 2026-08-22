## List All Restaurants and Their Dishes

```sql
SELECT
	r.name AS restaurant_name,
	r.city,
	d.dish_name,
	d.price
FROM restaurants AS r
LEFT JOIN dishes AS d
	ON r.id = d.restaurant_id;
```
