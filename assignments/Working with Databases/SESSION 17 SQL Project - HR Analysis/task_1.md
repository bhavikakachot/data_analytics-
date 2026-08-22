## Create the `Restaurant` Table

```sql
CREATE TABLE Restaurant (
	id INT PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	cuisine VARCHAR(100) NOT NULL,
	location VARCHAR(255) NOT NULL,
	average_rating DECIMAL(2, 1) NOT NULL
);
```

Insert popular Zomato-style restaurant records:

```sql
INSERT INTO Restaurant (
	id,
	name,
	cuisine,
	location,
	average_rating
)
VALUES
	(1, 'Indian Accent', 'Indian', 'New Delhi', 4.8),
	(2, 'The Bombay Canteen', 'Modern Indian', 'Mumbai', 4.7),
	(3, 'Paradise Biryani', 'Hyderabadi', 'Hyderabad', 4.5),
	(4, 'Bademiya', 'North Indian', 'Mumbai', 4.3),
	(5, 'Social', 'Continental', 'Bengaluru', 4.2);
```
