-- Full Info for Address








CREATE OR REPLACE FUNCTION sp_courses_by_address(
	address_name VARCHAR(100)
) 
AS
$$
BEGIN
	TRUNCATE search_results;

	INSERT INTO serach_results(
		address_name,
		full_name,
		level_of_bill,
		make,
		condition,
		category_name
	)
	SELECT
		address_name,
		cl.full_name,
		CASE
			WHEN co.bill <= 20 THEN 'Low'
			WHEN co.bill <= 30 THEN 'Medium'
			ELSE 'High'
		END,
			
	FROM
		addresses AS a
	JOIN
		courses AS co
	ON
		a.id = co.from_address_id
	JOIN
		cars AS cr
	ON	
		cr.id = co.car_id
	JOIN
		categories AS ca
	ON
		ca.id = cr.category_id
	JOIN
		clients AS cl
	ON
		cl.id = co.client_id
	WHERE	
		a.name = address_name
	ORDER BY 
		cr.make,
		cl.full_name;
END;
$$
LANGUAGE plpgsql;