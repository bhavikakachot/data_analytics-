## Installing PostgreSQL and Creating the Database

PostgreSQL can be installed by downloading the installer from the official PostgreSQL website. During installation, configure the username, password, and port number. The default port is `5432`.

After installation, open the PostgreSQL command-line tool, `psql`, and connect to the PostgreSQL server:

```bash
psql -U postgres
```

Create a new database named `music_streaming_app`:

```sql
CREATE DATABASE music_streaming_app;
```

To verify that the database was created successfully, list all available databases:

```sql
\l
```

Connect to the newly created database:

```sql
\c music_streaming_app
```

The `music_streaming_app` database is now ready for creating tables related to users, songs, artists, albums, playlists, and subscriptions.
