## Creating the `Orders` Table

```sql
CREATE TABLE Orders (
	order_id INT PRIMARY KEY,
	user_id INT,
	order_date DATE,
	total_amount DECIMAL(10, 2)
);
```

Insert sample food orders from different users and dates:

```sql
INSERT INTO Orders (order_id, user_id, order_date, total_amount)
VALUES
	(1, 201, '2026-08-01', 425.50),
	(2, 202, '2026-08-02', 289.00),
	(3, 203, '2026-08-04', 615.75),
	(4, 201, '2026-08-06', 350.25),
	(5, 204, '2026-08-09', 199.50),
	(6, 205, '2026-08-12', 780.00),
	(7, 202, '2026-08-15', 325.25);
```
