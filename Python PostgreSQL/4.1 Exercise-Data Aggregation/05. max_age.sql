-- Max Age

-- FIrst Way
SELECT
	max(age) AS maximum_age
FROM
	wizard_deposits;

-- Second Way
SELECT
	age AS maximum_age
FROM
	wizard_deposits
ORDER BY
	age DESC
LIMIT 1;    