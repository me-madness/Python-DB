-- Min Deposit Charge

-- FIrst Way
SELECT
	min(deposit_charge) AS minimum_deposit_charge
FROM
	wizard_deposits;

-- Second Way
SELECT 
	deposit_charge AS minimum_deposit_charge
FROM	
	wizard_deposits
ORDER BY
	deposit_charge
LIMIT 1;	