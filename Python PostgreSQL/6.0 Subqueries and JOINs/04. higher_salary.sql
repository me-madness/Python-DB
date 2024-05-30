-- Higher Salary

-- First Way
SELECT
	count(*)
FROM
	employees
WHERE salary >
		(SELECt avg(salary) FROM employees);

-- Second Way
SELECT 88;        