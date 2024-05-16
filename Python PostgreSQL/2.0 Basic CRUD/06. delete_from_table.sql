-- Delete from Table

DELETE FROM employees
WHERE department_id = 2 or department_id = 1
--WHERE department_id BETWEEN 1 and 2
--WHERE department_id IN (1, 2)
;

SELECT * FROM employees