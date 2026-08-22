## Create the `Review` Table

```sql
CREATE TABLE Review (
	id INT PRIMARY KEY,
	restaurant_id INT NOT NULL,
	user_name VARCHAR(255) NOT NULL,
	rating DECIMAL(2, 1) NOT NULL,
	review_date DATE NOT NULL,
	FOREIGN KEY (restaurant_id) REFERENCES Restaurant(id)
);
```

Insert sample reviews linked to restaurants:

```sql
INSERT INTO Review (
	id,
	restaurant_id,
	user_name,
	rating,
	review_date
)
VALUES
	(1, 1, 'Aarav Sharma', 5.0, '2026-07-01'),
	(2, 1, 'Meera Patel', 4.5, '2026-07-03'),
	(3, 2, 'Rohan Singh', 4.8, '2026-07-05'),
	(4, 2, 'Ananya Das', 4.2, '2026-07-08'),
	(5, 3, 'Kabir Khan', 4.7, '2026-07-10'),
	(6, 3, 'Ishita Rao', 4.4, '2026-07-12'),
	(7, 4, 'Vikram Joshi', 4.1, '2026-07-15'),
	(8, 4, 'Nisha Kapoor', 4.6, '2026-07-18'),
	(9, 5, 'Arjun Menon', 4.3, '2026-07-20'),
	(10, 5, 'Tara Iyer', 4.0, '2026-07-22');
```
