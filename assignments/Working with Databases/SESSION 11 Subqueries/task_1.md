## Restaurants Rated Above Their City Average

```sql
SELECT id, name, city, rating
FROM Restaurants AS r
WHERE r.rating > (
	SELECT AVG(city_restaurant.rating)
	FROM Restaurants AS city_restaurant
	WHERE city_restaurant.city = r.city
);
```
