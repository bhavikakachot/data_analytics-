## Payment Methods with High Average Orders

```sql
SELECT payment_method, AVG(amount) AS average_order_amount
FROM Orders
GROUP BY payment_method
HAVING AVG(amount) > 300;
```
