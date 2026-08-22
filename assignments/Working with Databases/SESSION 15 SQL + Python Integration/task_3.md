## Load Restaurants into a DataFrame

```python
import sqlite3

import pandas as pd

with sqlite3.connect('foodie.db') as connection:
	restaurants_df = pd.read_sql_query(
		'SELECT * FROM Restaurants',
		connection
	)

print(restaurants_df.head(2))
```
