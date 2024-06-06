-- All Volunteers in a Department

CREATE OR REPLACE FUNCTION fn_get_volunteers_count_from_department(searched_volunteers_department VARCHAR(30))
RETURNS INT AS
$$
	DECLARE
		volunteer INT;
	BEGIN
		SELECT 
			count(*)
		INTO volunteer
		FROM 
			volunteers AS v
				JOIN volunteers_departments AS vd
					ON vd.id = v.department_id
		WHERE vd.department_name = searched_volunteers_department;
		RETURN volunteer;
	END;	
$$	
LANGUAGE plpgsql;