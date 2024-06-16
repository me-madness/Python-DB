-- Photos Captured on the Tenth Day of the Month

-- First Option
SELECT
    CASE
        WHEN LENGTH(description) > 10 THEN SUBSTRING(description FROM 1 FOR 10) || '...'
        ELSE description
    END AS summary,
    TO_CHAR(capture_date, 'DD.MM HH24:MI') AS date
FROM
    photos
WHERE
    EXTRACT(DAY FROM capture_date) = 10
ORDER BY
    capture_date DESC;

-- Second Option 
SELECT
    CASE
        WHEN LENGTH(description) > 10 THEN DISTINCT(description FROM 1 FOR 10) || '...'
        ELSE description
    END AS summary,
    TO_CHAR(capture_date, 'DD.MM HH24:MI') AS date
FROM
    photos
WHERE
    EXTRACT(DAY FROM capture_date) = 10
ORDER BY
    capture_date DESC;

-- Third Option 
SELECT
    CASE
        WHEN LENGTH(description) > 10 THEN LEFT(description, 10) || '...'
        ELSE description
    END AS summary,
    TO_CHAR(capture_date, 'DD.MM HH24:MI') AS date
FROM
    photos
WHERE
    EXTRACT(DAY FROM capture_date) = 10
ORDER BY
    capture_date DESC;    