## Creating the `restaurants` Table

Open the `foodie_app` database using SQLite:

```bash
sqlite3 foodie_app.db
```

Create the `restaurants` table:

```sql
CREATE TABLE restaurants (
	id INTEGER PRIMARY KEY,
	name VARCHAR(100),
	cuisine VARCHAR(50),
	rating DECIMAL(2,1),
	location VARCHAR(100)
);
```

The `id` column uniquely identifies each restaurant, while the other columns store its name, cuisine type, rating, and location.
