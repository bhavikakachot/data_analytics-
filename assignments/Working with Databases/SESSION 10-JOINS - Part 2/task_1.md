## Creating the `Influencers` and `Collaborations` Tables

```sql
CREATE TABLE Influencers (
	id INTEGER PRIMARY KEY,
	name TEXT NOT NULL
);

CREATE TABLE Collaborations (
	id INTEGER PRIMARY KEY,
	influencer1_id INTEGER,
	influencer2_id INTEGER,
	collab_date DATE,
	FOREIGN KEY (influencer1_id) REFERENCES Influencers(id),
	FOREIGN KEY (influencer2_id) REFERENCES Influencers(id)
);
```

## List Influencers and Collaboration Partners

The `FULL JOIN` keeps influencers who appear in either collaboration column and also keeps influencers with no matching collaboration. The `CASE` expression displays the other influencer as the collaboration partner:

```sql
SELECT
	i.name AS influencer_name,
	CASE
		WHEN i.id = c.influencer1_id THEN influencer2.name
		ELSE influencer1.name
	END AS collaboration_partner,
	c.collab_date
FROM Influencers AS i
FULL JOIN Collaborations AS c
	ON i.id = c.influencer1_id
	OR i.id = c.influencer2_id
LEFT JOIN Influencers AS influencer1
	ON c.influencer1_id = influencer1.id
LEFT JOIN Influencers AS influencer2
	ON c.influencer2_id = influencer2.id;
```

Influencers without collaborations appear with `NULL` for `collaboration_partner` and `collab_date`.
