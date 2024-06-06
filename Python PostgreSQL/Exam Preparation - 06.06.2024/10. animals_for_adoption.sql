-- Animals for Adoption

SELECT
	a.name AS animal,
	EXTRACT('year' FROM birthdate) AS birth_year,
	at.animal_type
FROM
	animals AS a
		JOIN animal_types AS at
			ON a.animal_type_id = at.id
WHERE 
	at.animal_type <> 'Birds'
	and age('01/01/2022', a.birthdate) < '5 years'
	and a.owner_id IS NULL
ORDER BY a.name;