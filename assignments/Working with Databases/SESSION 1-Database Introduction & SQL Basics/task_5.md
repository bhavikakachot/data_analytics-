## Difference Between a Table, Row, and Column in SQL

In a food delivery application such as Zomato, a **table** is used to store related data in an organized format. For example, a `restaurants` table could store information about restaurants available on the platform.

A **column** represents one type of information or attribute. The `restaurants` table might contain columns such as `restaurant_id`, `restaurant_name`, `cuisine`, and `location`.

A **row** represents one complete record in the table. For example, one row could contain the details of a single restaurant:

| restaurant_id | restaurant_name | cuisine | location |
|---|---|---|---|
| 101 | Spice Garden | Indian | Mumbai |

In this example, the entire `restaurants` structure is the **table**, each vertical field such as `cuisine` is a **column**, and the complete record for Spice Garden is a **row**. A table contains multiple rows, while each row contains a value for every column.
