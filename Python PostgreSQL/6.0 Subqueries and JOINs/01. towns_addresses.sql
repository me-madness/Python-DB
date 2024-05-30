-- Towns Addresses

SELECT
	t.town_id,
	t.name as town_name,
	a.address_text
FROM
	towns as t
		JOIN addresses as a
			ON t.town_id = a.address_id
ORDER BY t.town_id, a.address_id;