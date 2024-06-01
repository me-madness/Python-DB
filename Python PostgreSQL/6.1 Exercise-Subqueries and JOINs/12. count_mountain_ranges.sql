-- Count Mountain ranges

SELECT
	mc.country_code,
	COUNT(m.mountain_range) AS mountain_rage_count
FROM
	mountains_countries AS mc
JOIN
	mountains AS m
ON
	m.id = mc.mountain_id
WHERE 
	mc.country_code IN ('US', 'RU', 'BG')
GROUP BY
	mc.country_code
ORDER BY
	mountain_rage_count DESC;