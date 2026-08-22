
```sql
WITH cleaned_restaurants AS (
	SELECT
		CAST(REPLACE(approx_cost_for_two, ',', '') AS DECIMAL(10, 2)) AS cost_for_two
	FROM zomato_restaurants
	WHERE approx_cost_for_two IS NOT NULL
		AND approx_cost_for_two NOT IN ('-', '')
),
segmented_restaurants AS (
	SELECT
		CASE
			WHEN cost_for_two < 400 THEN 'Budget'
			WHEN cost_for_two BETWEEN 400 AND 800 THEN 'Mid-range'
			WHEN cost_for_two > 800 THEN 'Premium'
		END AS market_segment
	FROM cleaned_restaurants
)
SELECT
	market_segment,
	COUNT(*) AS restaurant_count
FROM segmented_restaurants
GROUP BY market_segment
ORDER BY CASE market_segment
	WHEN 'Budget' THEN 1
	WHEN 'Mid-range' THEN 2
	WHEN 'Premium' THEN 3
END;
```
