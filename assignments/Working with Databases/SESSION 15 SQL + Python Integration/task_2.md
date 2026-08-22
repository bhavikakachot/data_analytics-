## Insert and Query Restaurants

```python
import sqlite3

restaurants = [
	(1, 'Spice Route', 'Indian', 4.6),
	(2, 'Pasta House', 'Italian', 3.9),
	(3, 'Sushi World', 'Japanese', 4.3)
]

with sqlite3.connect('foodie.db') as connection:
	connection.executemany('''
		INSERT OR IGNORE INTO Restaurants (id, name, cuisine, rating)
		VALUES (?, ?, ?, ?)
	''', restaurants)

	result = connection.execute('''
		SELECT name
		FROM Restaurants
		WHERE rating > 4.0
		ORDER BY rating DESC
	''')

	for (name,) in result:
		print(name)
```
