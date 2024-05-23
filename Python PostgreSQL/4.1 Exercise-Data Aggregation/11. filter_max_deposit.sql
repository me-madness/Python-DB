-- Filter max deposit

SELECT
	magic_wand_creator,
	max(deposit_amount) AS max_deposit_amount
FROM
	wizard_deposits
GROUP BY magic_wand_creator
HAVING max(deposit_amount) NOT BETWEeN 20000 and 40000
ORDER BY max_deposit_amount DESC	
LIMIT 3;