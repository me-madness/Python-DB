-- Top 3 Most Commented Photos

SELECT
	p.id AS photo_id,
	p.capture_date,
	p.description,
	COUNT(c.content) AS comments_count
FROM 
	photos AS p
JOIN
	comments AS c
ON
	p.id = c.photo_id
WHERE 	
	p.description IS NOT NULL 
		AND 
	p.description <> ''	
GROUP BY
	p.id,
	p.capture_date,
	p.description
ORDER BY 
	comments_count DESC,
	p.id ASC
LIMIT 3;