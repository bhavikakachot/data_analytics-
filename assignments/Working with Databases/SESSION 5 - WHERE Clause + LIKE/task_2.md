## Finding Highly Rated Restaurants by City

```sql
SELECT *
FROM Restaurants
WHERE rating > 4.0
	AND city IN ('Ahmedabad', 'Surat');
```
