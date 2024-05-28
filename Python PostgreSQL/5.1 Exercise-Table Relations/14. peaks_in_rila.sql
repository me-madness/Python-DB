-- Peaks in Rila

SELECT
	mountain_range,
	peak_name,
	elevation
FROM
	peaks
JOIN
	mountains
ON
	peaks.mountain_id = mountains.id
WHERE
	mountain_range LIKE '%Rila%'
	-- TRIM(mountain_range) = 'Rila'
ORDER BY
	elevation DESC;