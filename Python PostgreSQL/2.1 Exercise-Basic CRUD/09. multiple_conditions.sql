-- Multiple Conditions

SELECT
	number,
	stree
FROM
	addresses
WHERE
	ID BETWEEN 50 AND 100
		OR
	number < 1000;