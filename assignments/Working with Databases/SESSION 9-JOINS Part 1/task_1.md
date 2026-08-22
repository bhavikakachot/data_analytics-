## Creating the `restaurants` and `dishes` Tables

```sql
CREATE TABLE restaurants (
	id INTEGER PRIMARY KEY,
	name TEXT,
	city TEXT
);

CREATE TABLE dishes (
	id INTEGER PRIMARY KEY,
	restaurant_id INTEGER,
	dish_name TEXT,
	price DECIMAL(10, 2),
	FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
);
```

Insert three restaurants:

```sql
INSERT INTO restaurants (id, name, city)
VALUES
	(1, 'Spice Garden', 'Mumbai'),
	(2, 'The Green Bowl', 'Bengaluru'),
	(3, 'Coastal Bites', 'Chennai');
```

Insert three dishes for each restaurant:

```sql
INSERT INTO dishes (id, restaurant_id, dish_name, price)
VALUES
	(1, 1, 'Paneer Tikka', 280.00),
	(2, 1, 'Butter Naan', 80.00),
	(3, 1, 'Veg Biryani', 240.00),
	(4, 2, 'Quinoa Salad', 320.00),
	(5, 2, 'Avocado Toast', 260.00),
	(6, 2, 'Berry Smoothie', 180.00),
	(7, 3, 'Fish Curry', 420.00),
	(8, 3, 'Prawn Fry', 450.00),
	(9, 3, 'Lemon Rice', 160.00);
```
