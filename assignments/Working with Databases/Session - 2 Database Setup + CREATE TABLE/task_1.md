## Installing and Verifying SQLite

SQLite can be installed by downloading the SQLite command-line tools from the official SQLite website and adding the folder containing `sqlite3` to the system PATH.

Open Command Prompt or a terminal and verify that SQLite is installed:

```bash
sqlite3 --version
```

If the installation is successful, the command displays the installed SQLite version. Create or open a database file using:

```bash
sqlite3 music_streaming_app.db
```

Inside the SQLite command-line interface, verify the connection and SQLite version:

```sql
.databases
SELECT sqlite_version();
```

The `.databases` command displays the connected database file, while `SELECT sqlite_version();` confirms that SQLite is working correctly. Exit the SQLite interface with:

```sql
.quit
```
