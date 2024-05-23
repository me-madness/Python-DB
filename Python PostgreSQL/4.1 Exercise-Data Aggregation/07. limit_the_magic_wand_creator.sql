-- Limit the Magic Wand creator

SELECT
	magic_wand_creator,
	min(magic_wand_size) AS minimum_wand_size
FROM
	wizard_deposits
GROUP BY magic_wand_creator
ORDER BY minimum_wand_size
LIMIT 1;