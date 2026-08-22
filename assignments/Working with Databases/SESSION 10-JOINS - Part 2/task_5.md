## List Products with Category Names

Assuming `Products` has `id`, `name`, and `category_id` columns, and `Categories` has `id` and `name` columns.

### Query 1: Direct Key Equality

```sql
SELECT
	p.name AS product_name,
	c.name AS category_name
FROM Products AS p
LEFT JOIN Categories AS c
	ON p.category_id = c.id;
```

### Query 2: Casted Key Comparison

```sql
SELECT
	p.name AS product_name,
	c.name AS category_name
FROM Products AS p
LEFT JOIN Categories AS c
	ON CAST(p.category_id AS TEXT) = CAST(c.id AS TEXT);
```

Query 1 is more efficient because direct equality on matching key types can use an index, while casting both columns adds work and may prevent efficient index use.
