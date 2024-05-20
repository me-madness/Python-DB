-- Tear of Birth

SELECT 
	first_name,
	last_name,
	EXTRACT('year' FROM born) AS YEAR
FROM authors;