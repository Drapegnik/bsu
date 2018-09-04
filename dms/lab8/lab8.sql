-- 1. Создайте таблицу `emp_tel`, с полями `empno`, `phone_num`.
-- - Первое из них - поле идентичное полю `empno` таблицы `emp` и служит внешним ключом для связывания таблиц `emp` и `emp_tel`.
-- - Второе поле – массив переменной длины с максимальным числом элементов равным четырём.
-- - Поле может содержать телефоны сотрудника (рабочий, `mts`, `velcome`, `life`).
DROP TABLE emp_tel;
/
CREATE OR REPLACE TYPE phone_num_ty AS VARRAY(4) OF VARCHAR2(30);
/
CREATE TABLE emp_tel (
  empno INTEGER NOT NULL REFERENCES emp(empno),
  phone_num phone_num_ty
);

-- 2. Вставьте записи в таблицу `emp_tel` со следующими данными:
-- ```
--  505, 2203415, 80297121314, 80296662332, NULL
--  303, 2240070, 80297744543, 80296667766, 80443345543
--  503, 2233014, NULL, 80296171717, 80443161612
--  104, 22333015, 80297654321, NULL, 90443939398
-- ```
INSERT INTO  emp_tel VALUES(505, phone_num_ty('2203415', '80297121314', '80296662332', NULL));
INSERT INTO  emp_tel VALUES(303, phone_num_ty('2240070', '80297744543', '80296667766', '80443345543'));
INSERT INTO  emp_tel VALUES(503, phone_num_ty('2233014', NULL, '80296171717', '80443161612'));
INSERT INTO  emp_tel VALUES(104, phone_num_ty('22333015', '80297654321', NULL, '90443939398'));

-- 3. Создайте запросы:
-- - a) для сотрудников с номерами `104`, `303` указать имена и номера телефонов.
SELECT emp.empname, emp_tel.phone_num
FROM emp_tel
JOIN emp ON emp.empno = emp_tel.empno
WHERE emp.empno IN (104, 303);

-- - b) для сотрудника с номером `505`, используя функцию `TABLE`, укажите его номер и телефоны.
SELECT emp_tel.empno, column_value FROM emp_tel, TABLE(phone_num) WHERE emp_tel.empno = 505;

-- 4. Создайте таблицу `children` с полями `empno`, `child`.
-- - Первое из них - поле идентичное полю `empno` таблицы `emp` и служит внешним ключом для связывания таблиц `emp` и `children`.
-- - Второе является вложенной таблицей и содержит данные об имени (`name`) и дате рождения ребёнка (`birthdate`) сотрудника.
DROP TABLE children;
/
DROP TYPE clildren_table_ty;
/
CREATE OR REPLACE TYPE clildren_record_ty AS OBJECT (
  name VARCHAR(50),
  birthdate DATE
);
/
CREATE TYPE clildren_table_ty IS TABLE OF clildren_record_ty;
/
CREATE TABLE children (
  empno NUMBER NOT NULL REFERENCES emp(empno),
  child clildren_table_ty
) NESTED TABLE child STORE AS child_table;

-- 5. Вставьте в таблицу `children` записи:
-- - a) для сотрудника с номером `102` двое детей:
-- ```
--  Jack, 02.02.2000
--  Mari, 10.11.2004
-- ```
INSERT INTO children VALUES(
  102,
  clildren_table_ty(
    clildren_record_ty('Jack', TO_DATE('02-02-2000','dd-mm-yyyy')),
    clildren_record_ty('Mari', TO_DATE('10-11-2004','dd-mm-yyyy'))
  )
);

-- - b) для сотрудника с номером `327` двое детей:
-- ```
--  Alex, 22.09.2005
--  Janis, 04.10.2008
-- ```
INSERT INTO children VALUES(
  327,
  clildren_table_ty(
    clildren_record_ty('Alex', TO_DATE('22-09-2005','dd-mm-yyyy')),
    clildren_record_ty('Janis',TO_DATE('04-10-2008','dd-mm-yyyy'))
  )
);

-- 6. Создайте запросы:
-- - a) укажите все сведения из таблицы `children`
SELECT temp.empno, tchild.* FROM children temp, TABLE(temp.child) tchild;

-- - b) укажите номер сотрудника, имеющего ребёнка с именем `Janis`, имя ребёнка и дату рождения ребёнка.
SELECT temp.empno, tchild.* FROM children temp, TABLE(temp.child) tchild WHERE name = 'Janis';

-- 7. Измените дату рождения ребёнка с именем `Alex` на `10.10.2006`.
UPDATE TABLE (
  SELECT child FROM children, TABLE(child) tchild
  WHERE tchild.name = 'Alex'
)
SET birthdate = TO_DATE('10-10-2006', 'dd-mm-yyyy') WHERE name = 'Alex';
SELECT temp.empno, tchild.* FROM children temp, TABLE(temp.child) tchild;

-- 8. Добавьте для сотрудника с номером `102` ребёнка с именем `Julio` и датой рождения `01.12.2010`.
INSERT INTO TABLE (
  SELECT child FROM children
  WHERE empno = 102
) VALUES (clildren_record_ty('Julio', TO_DATE('01.12.2010','dd.mm.yyyy')));
SELECT temp.empno, tchild.* FROM children temp, TABLE(temp.child) tchild;

-- 9. Удалите сведения о ребёнке с именем `Mari` для сотрудника с номером `102`.
DELETE FROM TABLE (
  SELECT child FROM children WHERE empno = 102
) temp where temp.name = 'Mari';
SELECT temp.empno, tchild.* FROM children temp, TABLE(temp.child) tchild;
