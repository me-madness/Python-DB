-- Format Date of Birth

SELECT 
	last_name,
	to_char(born, 'DD (DY Mon YYYY') AS "Date of Birth"
FROM authors;	