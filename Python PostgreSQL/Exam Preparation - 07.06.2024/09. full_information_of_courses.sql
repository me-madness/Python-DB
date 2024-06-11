-- Full Information of Courses

SELECT 

FROM
    courses AS c
JOIN
    clients AS cl
ON 
    c.client_id - cl.id
JOIN
    cars AS cr
ON
    cr.id = car_id
JOIN
    ca                    