-- Task 01

CREATE OR REPLACE FUNCTION fn_full_name(
	VARCHAR, VARCHAR
)
RETURNS VARCHAR AS 
$$
	BEGIN
		RETURN CONCAT($1, ' ', $2);
	END;
$$
LANGUAGE plpgsql;

SELECT * FROM fn_full_name('Cvetan', 'Tomov')

-- TAsk 02

CREATE OR REPLACE FUNCTION (
	
)
RETURNS VARCHAR AS 
$$
	BEGIN
		
	END;
$$
LANGUAGE plpgsql;

-- Task 03


