-- Lucky Accounts

SELECT
	CONCAT(a.id, ' ', a.username) AS id_username,
	a.email
FROM
	accounts AS a
JOIN
	accounts_photos AS ap
ON 
	a.id = ap.photo_id
WHERE 
	ap.account_id = ap.photo_id
ORDER BY
	id_username ASC;