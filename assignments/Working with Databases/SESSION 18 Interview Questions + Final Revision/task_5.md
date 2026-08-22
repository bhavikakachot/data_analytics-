## Optimizing a Flipkart Product Filter

1. **Create a composite index on the filter columns.**

	```sql
	CREATE INDEX idx_products_category_price
	ON Products (category, price);
	```

	This lets the database quickly locate products in the requested category and then narrow those results by price instead of scanning the entire table.

2. **Use a sargable filter and select only required columns.**

	```sql
	SELECT product_id, product_name, category, price
	FROM Products
	WHERE category = 'Electronics'
	  AND price BETWEEN 10000 AND 50000;
	```

	Direct comparisons allow the index to be used efficiently. Selecting specific columns also reduces the amount of data read and returned compared with `SELECT *`.
