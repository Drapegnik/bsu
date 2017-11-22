--1. Составьте программу вычисления налога и вставки его в таблицу `bonus`:
--1a. C помощью простого цикла (`LOOP`) с курсором, оператора `IF` и опретора `CASE`:
DECLARE
CURSOR bonusCursor IS
SELECT bonuscopy.empno,
       bonuscopy.month,
       bonuscopy.year,
       sum(bonus.bonvalue) AS sumbonvalue
FROM bonus bonuscopy
JOIN bonus ON bonus.empno = bonuscopy.empno
AND bonus.year = bonuscopy.year
AND bonus.month <= bonuscopy.month
GROUP BY bonuscopy.empno,
         bonuscopy.month,
         bonuscopy.year;

i bonusCursor % ROWTYPE;
taxPercent REAL := 0;
BEGIN OPEN bonusCursor;
  LOOP FETCH bonusCursor INTO i;
    EXIT WHEN bonusCursor % NOTFOUND;

    IF i.sumbonvalue <= 500 THEN taxPercent := 0.09;
    ELSIF i.sumbonvalue <= 1000 THEN taxPercent := 0.12;
    ELSE taxPercent := 0.15;
    END IF;

    UPDATE bonus
    SET tax = bonvalue * taxPercent
    WHERE empno = i.empno
      AND YEAR = i.year
      AND MONTH = i.month;
  END LOOP;
CLOSE bonusCursor;
END;
/
SELECT * FROM bonus;

--1b. С помощью курсорного цикла `FOR`:
DECLARE
CURSOR bonusCursor IS
SELECT bonuscopy.empno,
       bonuscopy.month,
       bonuscopy.year,
       sum(bonus.bonvalue) AS sumbonvalue
FROM bonus bonuscopy
JOIN bonus ON bonus.empno = bonuscopy.empno
AND bonus.year = bonuscopy.year
AND bonus.month <= bonuscopy.month
GROUP BY bonuscopy.empno,
         bonuscopy.month,
         bonuscopy.year;

taxPercent REAL := 0;

BEGIN
  FOR i IN bonusCursor LOOP
    IF i.sumbonvalue <= 500 THEN taxPercent := 0.09;
    ELSIF i.sumbonvalue <= 1000 THEN taxPercent := 0.12;
    ELSE taxPercent := 0.15;
    END IF;

    UPDATE bonus
    SET tax = bonvalue * taxPercent
    WHERE empno = i.empno
      AND YEAR = i.year
      AND MONTH = i.month;
  END LOOP;
END;
/
SELECT * FROM bonus;

--1с. С помощью курсора с параметром, передавая номер сотрудника, для которого необходимо посчитать налог.
CREATE OR REPLACE PROCEDURE task1c(employee IN INTEGER) IS
  CURSOR bonusCursor (employee INTEGER) IS
  SELECT bonuscopy.empno,
         bonuscopy.month,
         bonuscopy.year,
         sum(bonus.bonvalue) AS sumbonvalue
  FROM bonus bonuscopy
  JOIN bonus ON bonus.empno = bonuscopy.empno
  AND bonus.year = bonuscopy.year
  AND bonus.month <= bonuscopy.month
  WHERE bonuscopy.empno = employee
  GROUP BY bonuscopy.empno,
           bonuscopy.month,
           bonuscopy.year;

  i bonusCursor % ROWTYPE;
  taxPercent REAL := 0;
  BEGIN OPEN bonusCursor(employee);
    LOOP FETCH bonusCursor INTO i;
      EXIT WHEN bonusCursor % NOTFOUND;

      IF i.sumbonvalue <= 500 THEN taxPercent := 0.09;
      ELSIF i.sumbonvalue <= 1000 THEN taxPercent := 0.12;
      ELSE taxPercent := 0.15;
      END IF;

      UPDATE bonus
      SET tax = bonvalue * taxPercent
      WHERE empno = i.empno
        AND YEAR = i.year
        AND MONTH = i.month;
    END LOOP;
  CLOSE bonusCursor;
END task1c;
/
CALL task1c(101);
SELECT * FROM bonus WHERE empno = 101;

--2. Оформите составленные программы в виде процедур.
--2a.
CREATE OR REPLACE PROCEDURE task2a IS
  CURSOR bonusCursor IS
  SELECT bonuscopy.empno,
         bonuscopy.month,
         bonuscopy.year,
         sum(bonus.bonvalue) AS sumbonvalue
  FROM bonus bonuscopy
  JOIN bonus ON bonus.empno = bonuscopy.empno
  AND bonus.year = bonuscopy.year
  AND bonus.month <= bonuscopy.month
  GROUP BY bonuscopy.empno,
           bonuscopy.month,
           bonuscopy.year;

  i bonusCursor % ROWTYPE;
  taxPercent REAL := 0;

  BEGIN OPEN bonusCursor;
    LOOP FETCH bonusCursor INTO i;
      EXIT WHEN bonusCursor % NOTFOUND;
      IF i.sumbonvalue <= 500 THEN taxPercent := 0.09;
      ELSIF i.sumbonvalue <= 1000 THEN taxPercent := 0.12;
      ELSE taxPercent := 0.15;
      END IF;

      UPDATE bonus
      SET tax = bonvalue * taxPercent
      WHERE empno = i.empno
        AND YEAR = i.year
        AND MONTH = i.month;
    END LOOP;
  CLOSE bonusCursor;
END task2a;

/
EXECUTE task2a;
SELECT * FROM bonus;

--2b.
CREATE OR REPLACE PROCEDURE task2b IS
  CURSOR bonusCursor IS
  SELECT bonuscopy.empno,
         bonuscopy.month,
         bonuscopy.year,
         sum(bonus.bonvalue) AS sumbonvalue
  FROM bonus bonuscopy
  JOIN bonus ON bonus.empno = bonuscopy.empno
  AND bonus.year = bonuscopy.year
  AND bonus.month <= bonuscopy.month
  GROUP BY bonuscopy.empno,
           bonuscopy.month,
           bonuscopy.year;

  taxPercent REAL := 0;

  BEGIN
  FOR i IN bonusCursor LOOP
    IF i.sumbonvalue <= 500 THEN taxPercent := 0.09;
    ELSIF i.sumbonvalue <= 1000 THEN taxPercent := 0.12;
    ELSE taxPercent := 0.15;
    END IF;

    UPDATE bonus
    SET tax = bonvalue * taxPercent
    WHERE empno = i.empno
      AND YEAR = i.year
      AND MONTH = i.month;
  END LOOP;
END task1b;
/ 
EXECUTE task2b;
SELECT * FROM bonus;

--3. Создайте процедуру, вычисления налога и вставки его в таблицу `bonus` за всё время начислений для конкретного сотрудника.
--В качестве параметров передать проценты налога (до `500`, от `501` до `1000`, выше `1000`), номер сотрудника.
CREATE OR REPLACE PROCEDURE task3(taxPercent1 IN REAL, taxPercent2 IN REAL, taxPercent3 IN REAL, employee IN INTEGER) IS
  CURSOR bonusCursor (employee INTEGER) IS
  SELECT bonuscopy.empno,
         bonuscopy.month,
         bonuscopy.year,
         sum(bonus.bonvalue) AS sumbonvalue
  FROM bonus bonuscopy
  JOIN bonus ON bonus.empno = bonuscopy.empno
  AND bonus.year = bonuscopy.year
  AND bonus.month <= bonuscopy.month
  WHERE bonuscopy.empno = employee
  GROUP BY bonuscopy.empno,
           bonuscopy.month,
           bonuscopy.year;

  i bonusCursor % ROWTYPE;
  taxPercent REAL := 0;

  BEGIN OPEN bonusCursor(employee);
    LOOP FETCH bonusCursor INTO i;
      EXIT WHEN bonusCursor % NOTFOUND;
      IF i.sumbonvalue <= 500 THEN taxPercent := taxPercent1;
      ELSIF i.sumbonvalue <= 1000 THEN taxPercent := taxPercent2;
      ELSE taxPercent := taxPercent3;
      END IF;

      UPDATE bonus
      SET tax = bonvalue * taxPercent
      WHERE empno = i.empno
        AND YEAR = i.year
        AND MONTH = i.month;
    END LOOP;
  CLOSE bonusCursor;
END task3;

/ 
CALL task3(0, 0.15, 0.20, 102);
SELECT * FROM bonus WHERE empno = 102;

--4. Создайте функцию, вычисляющую суммарный налог на премию сотрудника за всё время начислений. 
--В качестве параметров передать процент налога (до `500`, от `501` до `1000`, выше `1000`), номер сотрудника.
--Возвращаемое значение – суммарный налог.
CREATE OR REPLACE FUNCTION task4(taxPercent1 IN REAL, taxPercent2 IN REAL, taxPercent3 IN REAL, employee IN INTEGER) RETURN REAL IS
  CURSOR bonusCursor (employee INTEGER) IS
  SELECT bonuscopy.empno,
         bonuscopy.month,
         bonuscopy.year,
         sum(bonus.bonvalue) AS sumbonvalue,
         avg(bonus.bonvalue) AS avgbonvalue
  FROM bonus bonuscopy
  JOIN bonus ON bonus.empno = bonuscopy.empno
  AND bonus.year = bonuscopy.year
  AND bonus.month <= bonuscopy.month
  WHERE bonuscopy.empno = employee
  GROUP BY bonuscopy.empno,
           bonuscopy.month,
           bonuscopy.year;

  i bonusCursor % ROWTYPE;
  taxPercent REAL := 0;
  total REAL := 0;

  BEGIN OPEN bonusCursor (employee);
    LOOP FETCH bonusCursor INTO i;
      EXIT WHEN bonusCursor % NOTFOUND;
      IF i.sumbonvalue <= 500 THEN taxPercent := taxPercent1;
      ELSIF i.sumbonvalue <= 1000 THEN taxPercent := taxPercent2;
      ELSE taxPercent := taxPercent3;
      END IF;
      total := total + i.avgbonvalue * taxPercent;
    END LOOP;
  CLOSE bonusCursor;
  RETURN total;
END task4;

/
SELECT task4(0, 0.15, 0.20, 102) FROM dual;
