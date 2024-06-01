-- Multiplication of Information

-- First Option
SELECT
	b.booking_id,
	c.first_name AS customer_name
FROM
	bookings AS b,
	customers AS c;

-- Second Option
SELECT
	b.booking_id,
	c.first_name AS customer_name
FROM
	bookings AS b
CROSS JOIN
    customers AS c
ORDER BY 
    customer_name;    