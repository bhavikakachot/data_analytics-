## Add Delivery Charges and Adjust Ratings

```python
import sqlite3

import pandas as pd

with sqlite3.connect('foodie.db') as connection:
	restaurants_df = pd.read_sql_query(
		'SELECT * FROM Restaurants',
		connection
	)

restaurants_df['delivery_charge'] = 50
restaurants_df['final_rating'] = restaurants_df.apply(
	lambda restaurant: restaurant['rating'] + 0.1
	if restaurant['cuisine'] == 'Italian'
	else restaurant['rating'],
	axis=1
)

print(restaurants_df)
```
