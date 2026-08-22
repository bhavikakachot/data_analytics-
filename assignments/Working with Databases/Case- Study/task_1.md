## Top 5 North Indian Restaurants in Koramangala

The query assumes the Kaggle data has been imported into a table named `zomato_restaurants` and that `rate` is stored in values such as `4.5/5`.

```sql
SELECT
	name,
	location,
	cuisines,
	CAST(REPLACE(rate, '/5', '') AS DECIMAL(3, 1)) AS rating
FROM zomato_restaurants
WHERE location LIKE '%Koramangala%'
	AND cuisines LIKE '%North Indian%'
	AND rate IS NOT NULL
	AND rate NOT IN ('-', 'NEW')
ORDER BY rating DESC
LIMIT 5;
```
