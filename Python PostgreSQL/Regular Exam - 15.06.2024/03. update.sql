-- Update

UPDATE addresses
SET  country (IF country LIKE 'B%' THEN
		country = 'Blocked';
	 ELSIF country LIKE 'T%' THEN
		country = 'Test'
	 ELSIF country LIKE 'P%' THEN
		country = 'In progress';
	 END IF);
UPDATE addresses
SET country = 
CASE 
	WHEN country LIKE 'B%' THEN country = 'Blocked'
	WHEN country LIKE 'T%' THEN country = 'Test'
	WHEN country LIKE 'P%' THEN country = 'In Progress'
END;
