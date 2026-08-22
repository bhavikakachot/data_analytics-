## Creating the `Orders` Table

```sql
CREATE TABLE Orders (
	order_id INT PRIMARY KEY,
	user_name VARCHAR(255),
	total_amount DECIMAL(10, 2),
	order_date DATE
);
```

Insert five sample orders, including one order with a `NULL` total amount:

```sql
INSERT INTO Orders (order_id, user_name, total_amount, order_date)
VALUES
	(1, 'Alice', 125.50, '2026-01-10'),
	(2, 'Bob', 89.99, '2026-01-12'),
	(3, 'Charlie', NULL, '2026-01-15'),
	(4, 'Diana', 240.00, '2026-01-18'),
	(5, 'Ethan', 57.25, '2026-01-20');
```
