CREATE OR REPLACE PACKAGE child_bonus AS FUNCTION get_child_bonus(employee IN INTEGER, x1 IN REAL, x2 IN REAL, x3 IN REAL) RETURN REAL;
PROCEDURE add_child_bonus(x1 IN REAL, x2 IN REAL, x3 IN REAL);
END child_bonus;
/
CREATE OR REPLACE PACKAGE BODY child_bonus AS
	PROCEDURE add_child_bonus(x1 IN REAL, x2 IN REAL, x3 IN REAL) IS
		CURSOR child_bonus_cursor IS
		SELECT salaryempno,
		       nvl(salary, 0) + nvl(bonusearnings, 0)
		FROM
		  ( SELECT career.empno AS salaryempno,
		           nvl(sum(nvl(minsalary, 0)), 0) AS salary
		   FROM career
		   JOIN job ON job.jobno = career.jobno
		   WHERE ( extract(YEAR
		                   FROM career.startdate) <= 2016 )
		     AND ( ( career.enddate IS NULL )
		          OR ( ( extract(YEAR
		                         FROM career.enddate) = 2016 )
		              AND ( extract(MONTH
		                            FROM career.enddate) = 12 ) )
		          OR ( extract(YEAR
		                       FROM career.enddate) > 2016 ) )
		   GROUP BY career.empno )
		LEFT OUTER JOIN
		  ( SELECT empno AS bonusempno,
		           nvl(sum(nvl(bonvalue, 0)), 0) AS bonusearnings
		   FROM bonus
		   WHERE bonus.year = 2016
		   GROUP BY empno ) ON salaryempno = bonusempno;

		employee INTEGER := 0;
		earnings REAL := 0;
		children INTEGER := 0;
		child_bonus REAL := 0;

		BEGIN 
      OPEN child_bonus_cursor;
      LOOP 
        FETCH child_bonus_cursor INTO employee, earnings;
        EXIT WHEN child_bonus_cursor % NOTFOUND;

        SELECT nchild INTO children
        FROM emp
        WHERE empno = employee;

        IF (children > 0) THEN 
          IF children = 1 THEN child_bonus := earnings * x1 / 100;
            ELSIF children = 2 THEN child_bonus := earnings * x2 / 100;
            ELSIF children > 2 THEN child_bonus := earnings * x3 / 100;
          END IF;

        INSERT INTO bonus
        VALUES (employee, 12, 2016, child_bonus, NULL);

        END IF;
      END LOOP;
		CLOSE child_bonus_cursor;
	END add_child_bonus;

	FUNCTION get_child_bonus(
		employee IN INTEGER, x1 IN REAL, x2 IN REAL, x3 IN REAL
	) RETURN REAL IS bonusearnings REAL := 0;

	salary REAL := 0;
	total REAL := 0;
	children INTEGER := 0;
	child_bonus REAL := 0;

	BEGIN 
		BEGIN
		SELECT nvl(sum(nvl(bonvalue, 0)), 0) INTO bonusearnings
		FROM bonus
		WHERE empno = employee
		  AND bonus.year = 2015
		GROUP BY empno;
		EXCEPTION WHEN no_data_found THEN bonusearnings := 0;
		END;

		BEGIN
		SELECT nvl(sum(nvl(minsalary, 0)), 0) INTO salary
		FROM career
		JOIN job ON job.jobno = career.jobno
		WHERE ( career.empno = employee )
		  AND ( extract(YEAR
		                FROM career.startdate) <= 2016 )
		  AND ( ( career.enddate IS NULL )
		       OR ( ( extract(YEAR
		                      FROM career.enddate) = 2016 )
		           AND ( extract(MONTH
		                         FROM career.enddate) = 12 ) )
		       OR ( extract(YEAR
		                    FROM career.enddate) > 2016 ) )
		GROUP BY career.empno;
		EXCEPTION WHEN no_data_found THEN salary := 0;
		END;

		BEGIN
		SELECT nchild INTO children
		FROM emp
		WHERE empno = employee;
		EXCEPTION WHEN no_data_found THEN children := 0;
		END;

		total := bonusearnings + salary;

		IF children = 1 THEN child_bonus := total * x1 / 100;
		ELSIF children = 2 THEN child_bonus := total * x2 / 100;
		ELSIF children > 2 THEN child_bonus := total * x3 / 100;
		END IF;

		RETURN child_bonus;
	END get_child_bonus;
END child_bonus;

--- PROCEDURE CALL
BEGIN
	child_bonus.add_child_bonus(10, 20, 30);
END;

--- FUNCTION CALL
DECLARE
v REAL;
BEGIN
  v := child_bonus.get_child_bonus(102, 11, 21, 31);
  DBMS_OUTPUT.PUT_LINE(v);
END;
