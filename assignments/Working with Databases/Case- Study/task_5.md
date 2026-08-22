## Top 10 Restaurant Chains by Number of Outlets

The query assumes the Kaggle data is stored in `zomato_restaurants`, where each row represents a restaurant listing and `location` identifies its outlet area.

```sql
SELECT
	name AS restaurant_chain,
	COUNT(DISTINCT location) AS outlet_count
FROM zomato_restaurants
WHERE name IS NOT NULL
	AND name <> ''
GROUP BY name
ORDER BY outlet_count DESC, restaurant_chain
LIMIT 10;
```

`COUNT(DISTINCT location)` avoids counting duplicate listings in the same area as separate outlets.
