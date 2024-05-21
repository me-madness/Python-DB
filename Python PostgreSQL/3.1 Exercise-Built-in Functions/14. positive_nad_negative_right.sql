-- Positive and Negative RIGHT

SELECT
	peak_name,
	RIGHT(peak_name, 4) AS positive_right, -- Get the first 4
	RIGHT(peak_name, -4) AS negative_right -- Get everything but the last 4
FROM
	peaks;