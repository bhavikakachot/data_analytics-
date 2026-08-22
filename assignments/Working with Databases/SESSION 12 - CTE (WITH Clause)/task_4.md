## Movie Booking Dates for the Next 7 Days

```sql
WITH RECURSIVE available_dates AS (
	SELECT CURRENT_DATE AS booking_date

	UNION ALL

	SELECT booking_date + INTERVAL 1 DAY
	FROM available_dates
	WHERE booking_date < CURRENT_DATE + INTERVAL 6 DAY
)
SELECT booking_date
FROM available_dates
ORDER BY booking_date;
```
