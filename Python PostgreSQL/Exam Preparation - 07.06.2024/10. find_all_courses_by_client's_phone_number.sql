-- Find all Courses by Client’s Phone Number

CREATE OR REPLACE FUNCTION fn_courses_by_client(
	phone_number VARCHAR(20)
) RETURN INT
AS
$$
BEGIN
	RETURN (
		SELECT
			COUNT(*)
		FROM
			clients AS cl
		JOIN
			courses AS co
		ON
			co.client_id = cl.id
		WHERE
			cl.phone_number = '(803 6386812'
	);
END;
$$
LANGUAGE plpgsql;