-- Get Accounts Photos Count

CREATE FUNCTION udf_accounts_photos_count(account_username VARCHAR(30))
RETURNS INT
BEGIN
    DECLARE photos_count INT;
    
    SELECT COUNT(*)
    INTO photos_count
    FROM photos
    WHERE username = account_username;
    
    RETURN photos_count;
END;