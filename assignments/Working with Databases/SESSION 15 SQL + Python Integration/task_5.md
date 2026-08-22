## Daily Top-Rated Restaurant Summary

```python
import sqlite3

import pandas as pd

with sqlite3.connect('foodie.db') as connection:
	top_rated_restaurants = pd.read_sql_query(
		'''
		SELECT *
		FROM Restaurants
		WHERE rating > ?
		ORDER BY rating DESC
		''',
		connection,
		params=(4.5,)
	)

top_rated_restaurants.to_csv(
	'top_rated_restaurants.csv',
	index=False
)

print('Daily summary saved to top_rated_restaurants.csv')
```
