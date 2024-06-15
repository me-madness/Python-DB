-- Update


UPDATE addresses
SET country = 
CASE 
	WHEN country LIKE 'B%' THEN country = 'Blocked'
	WHEN country LIKE 'T%' THEN country = 'Test'
	WHEN country LIKE 'P%' THEN country = 'In Progress'
END;


UPDATE addresses
SET country =
    CASE
        WHEN country LIKE 'B%' THEN 'Blocked'
        WHEN country LIKE 'T%' THEN 'Test'
        WHEN country LIKE 'P%' THEN 'In Progress'
        ELSE country
    END
WHERE
    country LIKE 'B%' OR country LIKE 'T%' OR country LIKE 'P%';