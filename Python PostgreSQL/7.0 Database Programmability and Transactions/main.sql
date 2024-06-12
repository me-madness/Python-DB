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
		full_name VARCHAR(30);
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

CREATE OR REPLACE FUNCTION fn_get_city_id(
	city VARCHAR
)
RETURNS INT AS 
$$
	DECLARE
		city_id int;
	BEGIN
		SELECT id FROM country WHERE country_name = city INTO city_id;
		RETURN city_id;
	END;
$$
LANGUAGE plpgsql;

SELECT id FROM country WHERE country_name = 'Germany'
SELECT * FROM fn_get_city_id('Germany')


-- Task 06

CREATE OR REPLACE FUNCTION fn_get_city_id(
	city VARCHAR
)
RETURNS INT AS 
$$
	DECLARE
		city_id int;
	BEGIN
		SELECT id FROM country WHERE country_name = city INTO city_id;
		RETURN city_id;
	END;
$$
LANGUAGE plpgsql;

INSERt INTO persons (id, first_name, last_name, country_id, department)
VALUES (
		1011,
		'Pencho',
		'Kubadinski',
		fn_get_city_id('Germany'),
		'Lov i ribolov'
)	

SELECT * FROM persons
ORDER BY id DESC
LIMIT 1


-- Task 07

DROP FUNCTION fn_get_city_id

CREATE OR REPLACE FUNCTION fn_get_city_id(
	IN city_name VARCHAR, OUT city_id INT
)
AS 
$$
	BEGIN
		SELECT id FROM country WHERE country_name = city_name INTO city_id;
	END;
$$
LANGUAGE plpgsql;

SELECT * FROM fn_get_city_id('Bulgaria')

-- Task 08

DROP FUNCTION fn_get_city_id

CREATE OR REPLACE FUNCTION fn_get_city_id(
	IN city_name VARCHAR, OUT city_id INT, STATUS INT
)
AS 
$$
	BEGIN
		SELECT id FROM country WHERE country_name = city_name INTO city_id;
		STATUS := 100;
	END;
$$
LANGUAGE plpgsql;

SELECT * FROM fn_get_city_id('Bulgaria')


-- Task 09

CREATE OR REPLACE FUNCTION fn_insert_data(
	id INT, name VARCHAR
)
RETURNS BOOLEAN AS 
$$
	DECLARE
	BEGIN
		INSERT INTO country(id, country_name)
		VALUES(id, name);
		EXCEPTION
			WHEN UNIQUE_VIOLATION THEN RETURN FALSE;
		RETURN TRUE;
	END;
$$
LANGUAGE plpgsql;

SELECT fn_insert_data(14, 'Bangladesh')

-- Task 10

CREATE OR REPLACE FUNCTION (
	
)
RETURNS VARCHAR AS 
$$
	BEGIN
		
	END;
$$
LANGUAGE plpgsql;

-- Task 11 - Returns Table

CREATE OR REPLACE FUNCTION fn_get_countrys(
	
)
RETURNS TABLE (id int, name VARCHAR) AS 
$$
	BEGIN
		RETURN (SELECT * FROM country);
	END;
$$
LANGUAGE plpgsql;

SELECT * FROM fn_get_countrys();

-- Task 12

CREATE OR REPLACE FUNCTION (
	
)
RETURNS VARCHAR AS 
$$
	BEGIN
		
	END;
$$
LANGUAGE plpgsql;

-- Task 13

CREATE OR REPLACE FUNCTION (
	
)
RETURNS VARCHAR AS 
$$
	BEGIN
		
	END;
$$
LANGUAGE plpgsql;