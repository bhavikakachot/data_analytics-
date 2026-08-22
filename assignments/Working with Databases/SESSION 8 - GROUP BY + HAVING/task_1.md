## Creating the `Orders` Table

```sql
CREATE TABLE Orders (
	order_id INTEGER PRIMARY KEY,
	user_id INTEGER,
	payment_method TEXT,
	amount DECIMAL(10, 2)
);
```

Insert eight sample orders using different users and payment methods:

```sql
INSERT INTO Orders (order_id, user_id, payment_method, amount)
VALUES
	(1, 101, 'UPI', 499.00),
	(2, 102, 'Card', 1250.50),
	(3, 103, 'Wallet', 799.99),
	(4, 104, 'COD', 350.00),
	(5, 105, 'UPI', 1899.00),
	(6, 106, 'Card', 649.50),
	(7, 107, 'Wallet', 275.25),
	(8, 108, 'COD', 999.00);
```
