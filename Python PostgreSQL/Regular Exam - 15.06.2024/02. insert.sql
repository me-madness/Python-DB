-- Insert 

INSERT INTO
	addresses(street, town, country, account_id)
SELECT	
	username,
	password,
	ip,
	age
FROM
	accounts AS ac
JOIN
	addresses AS ad
USING 
	(id);