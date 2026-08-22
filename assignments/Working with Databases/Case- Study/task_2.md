## 3 Most Expensive Cuisines in Bangalore

The query assumes the Kaggle data is stored in `zomato_restaurants` and that `approx_cost_for_two` contains the average cost for two people.

```sql
SELECT
	cuisines,
	ROUND(
		AVG(
			CAST(REPLACE(approx_cost_for_two, ',', '') AS DECIMAL(10, 2))
		),
		2
	) AS average_cost_for_two
FROM zomato_restaurants
WHERE listed_in_city = 'Bangalore'
	AND approx_cost_for_two IS NOT NULL
	AND approx_cost_for_two NOT IN ('-', '')
GROUP BY cuisines
ORDER BY average_cost_for_two DESC
LIMIT 3;
```
