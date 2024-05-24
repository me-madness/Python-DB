-- Update Employees Data

UPDATE employees
SET salary =
	CASE
		WHEN hire_date < '2015-01-16' THEN salary + 2500
		WHEN hire_date < '2020-03-04' THEN salary + 1500
		ELSE salary
	END,
job_title =
	CASE
		WHEN hire_date < '2015-01-16' THEN concat('Senior', job_title)
		WHEN hire_date < '2020-03-04' THEN cincat('Mid-', job_title)
		ELSE salary
	END;