## Low-Rated Restaurants Offering Online Delivery

The query assumes the Kaggle data is stored in `zomato_restaurants` and that `rate` contains values such as `2.8/5`.

```sql
WITH cleaned_restaurants AS (
	SELECT
		name,
		location,
		cuisines,
		approx_cost_for_two,
		CAST(REPLACE(rate, '/5', '') AS DECIMAL(3, 1)) AS rating
	FROM zomato_restaurants
	WHERE online_order = 'Yes'
		AND rate IS NOT NULL
		AND rate NOT IN ('-', 'NEW')
)
SELECT
	name,
	location,
	cuisines,
	approx_cost_for_two,
	rating
FROM cleaned_restaurants
WHERE rating < 3.0
ORDER BY rating ASC, name;
```

### Identify Patterns

Run this supporting query to identify clusters by location, cuisine, and price:

```sql
WITH cleaned_restaurants AS (
	SELECT
		location,
		cuisines,
		CAST(REPLACE(rate, '/5', '') AS DECIMAL(3, 1)) AS rating,
		CAST(REPLACE(approx_cost_for_two, ',', '') AS DECIMAL(10, 2)) AS cost_for_two
	FROM zomato_restaurants
	WHERE online_order = 'Yes'
		AND rate IS NOT NULL
		AND rate NOT IN ('-', 'NEW')
		AND approx_cost_for_two IS NOT NULL
		AND approx_cost_for_two NOT IN ('-', '')
)
SELECT
	location,
	cuisines,
	ROUND(AVG(cost_for_two), 2) AS average_cost_for_two,
	COUNT(*) AS low_rated_restaurants,
	ROUND(AVG(rating), 2) AS average_rating
FROM cleaned_restaurants
WHERE rating < 3.0
GROUP BY location, cuisines
ORDER BY low_rated_restaurants DESC, average_rating ASC;
```

### Suggested Marketing Strategy

Target clusters revealed by the supporting query. For locations with repeated low ratings, improve delivery coverage, preparation-time estimates, and packaging. For cuisine clusters, promote menu and quality improvements based on highly rated competitors. For expensive low-rated restaurants, introduce value combos and clearer portion descriptions. Respond to recurring complaints, request feedback after successful deliveries, and track ratings monthly before increasing promotional spending.
