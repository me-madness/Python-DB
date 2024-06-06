-- Owners and Their Animals

SELECT
	o.name AS owner,
	count(*) AS count_of_animals
FROM
	owners AS o
		JOIN animals AS a
			ON a.owner_id = o.id
GROUP BY owner
ORDER BY count_of_animals DESC, owner
LIMIT 5;