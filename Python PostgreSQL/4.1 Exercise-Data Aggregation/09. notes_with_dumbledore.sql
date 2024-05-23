-- Notes with Dumbledore

SELECT
	first_name,
	count(notes) AS last_name
FROM
	wizard_deposits
WHERE notes LIKE '%Dumbledore%'
GROUP BY first_name;