-- All Volunteers in a Department

-- First Option
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

-- Second Option
CREATE OR REPLACE FUNCTION fn_get_volunteers_count_from_department(searched_volunteers_department VARCHAR(30))
RETURNS INT AS
$$
	DECLARE
		volunteer INT;
	BEGIN
		RETURN(
		SELECT 
			count(*)
		FROM 
			volunteers AS v
				JOIN volunteers_departments AS vd
					ON vd.id = v.department_id
		WHERE vd.department_name = searched_volunteers_department
		);
	END;	
$$	
LANGUAGE plpgsql;

-- Third Option
CREATE OR REPLACE FUNCTION fn_get_volunteers_count_from_department(searched_volunteers_department VARCHAR(30))
RETURNS INT AS
$$
	DECLARE
		volunteer INT;
	BEGIN
		volunteer :=
			(SELECT 
				count(*)
			FROM 
				volunteers AS v
					JOIN volunteers_departments AS vd
						ON vd.id = v.department_id
			WHERE vd.department_name = searched_volunteers_department
		);
		RETURN volunteer;
	END;	
$$	
LANGUAGE plpgsql;