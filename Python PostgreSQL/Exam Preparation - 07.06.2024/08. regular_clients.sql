-- Regular Clients

SELECT 
    *
FROM
    Clients AS cl
JOIN
    courses AS co
ON
    cl.id = co.client_id        
WHERE
    SUBSTRING(cl.full_name, 2, 1) = 'a'    