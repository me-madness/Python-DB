-- Booked for Nights

-- First Option
SELECT
	a.address || ' ' || a.address_2 AS apartment_address,
	b.booked_for AS nights
FROM
	apartments AS a
JOIN
	bookings as b
USING
	(booking_id)
ORDER BY 
	a.apartment_id ASC;

-- Second Option
SELECT
	a.address || ' ' || a.address_2 AS apartment_address,
	b.booked_for AS nights
FROM
	apartments AS a
JOIN
	bookings as b
ON 
    a.booking_id = b.booking_id 
ORDER BY 
	a.apartment_id ASC;    