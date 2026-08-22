## Creating the `users` Table

Open the `foodie_app` database using SQLite:

```bash
sqlite3 foodie_app.db
```

Create the `users` table:

```sql
CREATE TABLE users (
	user_id INTEGER PRIMARY KEY,
	username TEXT NOT NULL UNIQUE,
	email TEXT NOT NULL UNIQUE,
	phone_number TEXT NOT NULL UNIQUE,
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

The `user_id` column uniquely identifies each user. `TEXT` is suitable for usernames, email addresses, and phone numbers because phone numbers can contain symbols, spaces, or leading zeros. The `UNIQUE` constraints prevent duplicate usernames, email addresses, and phone numbers. `created_at` stores the date and time when the user record is created.
