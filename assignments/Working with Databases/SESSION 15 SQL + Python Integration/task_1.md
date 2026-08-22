## Create the `foodie.db` Database

Python includes `sqlite3` in its standard library, so no separate installation is required.

```python
import sqlite3

connection = sqlite3.connect('foodie.db')
cursor = connection.cursor()

cursor.execute('''
	CREATE TABLE IF NOT EXISTS Restaurants (
		id INTEGER PRIMARY KEY,
		name TEXT NOT NULL,
		cuisine TEXT NOT NULL,
		rating REAL
	)
''')

connection.commit()
connection.close()

print('foodie.db created successfully.')
```
