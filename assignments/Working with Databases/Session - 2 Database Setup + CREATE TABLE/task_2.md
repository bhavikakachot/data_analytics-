## Creating the `foodie_app` Database

SQLite creates a database when a database file is opened. Run the following command in the terminal:

```bash
sqlite3 foodie_app.db
```

This command creates a new database file named `foodie_app.db`, or opens it if it already exists. Verify the connected database inside the SQLite command-line interface:

```sql
.databases
```

The output should show `foodie_app.db` as the active database. This database can now be used to simulate a Zomato-style food delivery backend.
