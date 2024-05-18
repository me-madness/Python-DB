-- Upper

SELECT * FROM projects

UPDATE
	projects
SET
	name = UPPER(name)
RETURNING *;