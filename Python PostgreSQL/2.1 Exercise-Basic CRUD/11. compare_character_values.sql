-- Compare Character Values

SELECT
	name,
	start_date
FROM
	projects
WHERE
	name IN ('Mountain', 'Road', 'Touring');