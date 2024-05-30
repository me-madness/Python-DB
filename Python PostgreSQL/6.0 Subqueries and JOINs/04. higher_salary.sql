-- Higher Salary

SELECT
	count(*)
FROM
	employees
WHERE salary >
		(SELECt avg(salary) FROM employees);