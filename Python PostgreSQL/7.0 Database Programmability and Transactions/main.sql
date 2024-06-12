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

SELECT * FROM fn_full_name('Cvetan', 'Tomov');

-- TAsk 02

CREATE OR REPLACE FUNCTION fn_full_name(
	VARCHAR, VARCHAR
)
RETURNS VARCHAR AS 
$$
	DECLARE
		first_name ALIAS FOR $1;
		last_name ALIAS FOR $2;
		greeting VARCHAr;
	BEGIN
		greeting := 'Hello'
		RETURN CONCAT(first_name, ' ', last_name)
	END;
$$
LANGUAGE plpgsql;

SELECT * FROM fn_full_name('Milko', 'Toshev')

-- Task 03

CREATE OR REPLACE FUNCTION (
	
)
RETURNS VARCHAR AS 
$$
	BEGIN
		
	END;
$$
LANGUAGE plpgsql;

-- Task 04

CREATE OR REPLACE FUNCTION (
	
)
RETURNS VARCHAR AS 
$$
	BEGIN
		
	END;
$$
LANGUAGE plpgsql;