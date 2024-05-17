-- Find The Addresses

SELECT
	id,
	CONCAT(
	' ',
	street
	) AS address,
	city_id
FROM
	addresses
WHERE
	id >= 20;