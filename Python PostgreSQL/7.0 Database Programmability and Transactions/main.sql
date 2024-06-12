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

CREATE OR REPLACE FUNCTION fn_get_name_len(
	name VARCHAR
)
RETURNS INT AS 
$$
	BEGIN
		RETURN length(name)
	END;
$$
LANGUAGE plpgsql;

SELECT * FROM fn_get_name_len('Koko');

-- Task 04

CREATE OR REPLACE FUNCTION fn_full_name(
	first_name VARCHAR, last_name VARCHAR
)
RETURNS VARCHAR AS 
$$
	DECLARE
		full_name VARCHAR(30)
	BEGIN
		IF first_name is NULL AND last_name is NULL THEN
			full_name := NULL;
		ELSIF first_name is NULL THEN
			full_name := last_name;
		ELSIF last_name is NULL THEN
			full_name := first_name;
		ELSE
			full_name := CONCAT(first_name, ' ', last_name);
		END IF;
		RETURN full_name;
	END;
$$
LANGUAGE plpgsql;

SELECT * FROM fn_full_name('Koko', NULL)

-- Task 05

CREATE OR REPLACE FUNCTION (
	
)
RETURNS VARCHAR AS 
$$
	BEGIN
		
	END;
$$
LANGUAGE plpgsql;

-- Task 06

CREATE OR REPLACE FUNCTION (
	
)
RETURNS VARCHAR AS 
$$
	BEGIN
		
	END;
$$
LANGUAGE plpgsql;

-- Task 07

CREATE OR REPLACE FUNCTION (
	
)
RETURNS VARCHAR AS 
$$
	BEGIN
		
	END;
$$
LANGUAGE plpgsql;

-- Task 08

CREATE OR REPLACE FUNCTION (
	
)
RETURNS VARCHAR AS 
$$
	BEGIN
		
	END;
$$
LANGUAGE plpgsql;