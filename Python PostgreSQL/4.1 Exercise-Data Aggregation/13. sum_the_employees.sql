-- Sum the Employees

SELECT 
	sum(CASE department_id WHEN 1 THEN 1 ELSE 0 END) AS "Engineering",
	sum(CASE department_id WHEN 2 THEN 1 ELSE 0 END) AS "Tool Design",
	sum(CASE department_id WHEN 3 THEN 1 ELSE 0 END) AS "Sales",
	sum(CASE department_id WHEN 4 THEN 1 ELSE 0 END) AS "Marketing",
	sum(CASE department_id WHEN 5 THEN 1 ELSE 0 END) AS "Purchasing",
	sum(CASE department_id WHEN 6 THEN 1 ELSE 0 END) AS "Research and Development",
	sum(CASE department_id WHEN 7 THEN 1 ELSE 0 END) AS "Production"
FROM employees;