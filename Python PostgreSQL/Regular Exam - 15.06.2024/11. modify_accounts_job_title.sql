-- Modify Accounts Job Title

CREATE PROCEDURE udp_modify_account(
    IN address_street VARCHAR(30),
    IN address_town VARCHAR(30)
)
BEGIN
    UPDATE accounts
    SET job_title = CONCAT('(Remote) ', job_title)
    WHERE address_street = address_street
      AND address_town = address_town
      AND job_title NOT LIKE '(Remote)%';
END;

-- I must add a second Option for this task

CREATE PROCEDURE udp_modify_account(

)
BEGIN 

END;