# How To Create aa Type

CREATE TYPE address AS (
	street VARCHAR(50),
	city VARCHAR(50),
	postalCode CHAR(4)
);

CREATE TABLE customers(
	id SERIAL PRIMARY KEY,
	customer_name VARCHAR(150),
	customer_address address
);

INSERT INTO
	customers(customer_name, customer_address)
VALUES
	('Rangel', ('8, rue Ermesinde', 'Echternach', '6437'));

SELECT
	(customer_address).street
FROM customers;	    