## Identifying and Fixing a SQL Error

Open the database using SQLite:

```bash
sqlite3 foodie_app.db
```

The following statement intentionally contains an error: a comma is missing after the `name` column.

```sql
CREATE TABLE restaurants_error_demo (
	id INTEGER PRIMARY KEY,
	name TEXT
	cuisine TEXT
);
```

SQLite reports an error similar to:

```text
near "cuisine": syntax error
```

The error occurs because every column definition, except the last one, must be separated by a comma. The corrected statement is:

```sql
CREATE TABLE restaurants_error_demo (
	id INTEGER PRIMARY KEY,
	name TEXT,
	cuisine TEXT
);
```

After running the corrected statement, verify that the table was created:

```sql
.tables
```

A screenshot can be taken showing the error message followed by the corrected SQL statement and successful table creation.
