## Creating the `Restaurants` Table

Create the `Restaurants` table:

```sql
CREATE TABLE Restaurants (
	id INTEGER PRIMARY KEY,
	name VARCHAR(100),
	cuisine VARCHAR(50),
	rating DECIMAL(2,1),
	city VARCHAR(100)
);
```

Insert sample restaurants that could appear on Zomato:

```sql
INSERT INTO Restaurants (id, name, cuisine, rating, city)
VALUES
	(1, 'The Spice Route', 'Indian', 4.6, 'Mumbai'),
	(2, 'Pasta Paradise', 'Italian', 4.3, 'Bengaluru'),
	(3, 'Sushi House', 'Japanese', 4.5, 'Delhi'),
	(4, 'Burger Junction', 'American', 4.1, 'Hyderabad'),
	(5, 'Green Leaf Cafe', 'Healthy', 4.4, 'Pune');
```
