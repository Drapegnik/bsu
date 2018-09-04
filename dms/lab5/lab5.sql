-- 1. Создайте триггер, который при добавлении или обновлении записи в таблице `emp`, должен отменять действие и сообщать об ошибке:
--    * если для сотрудника с семейным положением холост (s) в столбце `nchild` указывается данное, отличное от `NULL` или `0`;
--    * если для любого сотрудника указывается отрицательное количество детей.
CREATE OR REPLACE TRIGGER emp_trigger_task1
BEFORE INSERT OR UPDATE ON emp
FOR EACH ROW
BEGIN
  IF (:new.nchild < 0)
  THEN RAISE_APPLICATION_ERROR(-20000, 'number of childs cant be <0');
  END IF;

  IF (:new.mstat = 's' AND NOT(:new.nchild IS NULL OR :new.nchild = 0))
  THEN RAISE_APPLICATION_ERROR(-20000, 'number of childrens must be 0 or NULL for single person');
  END IF;
END;

-- 2. Создайте триггер, который при добавлении или обновлении записи в таблице `emp` должен:
--    * осуществлять вставку данного равного `0`, если для сотрудника с семейным положением холост (`s`) в столбце `nchild` указывается данное, отличное от `NULL` или `0`;
--    * осуществлять вставку данного `NULL`, если для любого сотрудника указывается отрицательное количество детей.
CREATE OR REPLACE TRIGGER emp_trigger_task2
BEFORE INSERT OR UPDATE ON emp
FOR EACH ROW
BEGIN
  IF (:new.nchild < 0)
  THEN :new.nchild := NULL;
  END IF;

  IF (:new.mstat = 's' AND NOT(:new.nchild IS NULL OR :new.nchild = 0))
  THEN :new.nchild := 0;
  END IF;
END;

-- 3. Создайте триггер, который при обновлении записи в таблице `emp` должен отменять действие и сообщать об ошибке, если для сотрудников, находящихся в браке (`m`) в столбце `nchild` новое значение отличается от текущего более чем на `1`.
CREATE OR REPLACE TRIGGER emp_trigger_task3
BEFORE UPDATE ON emp FOR EACH ROW
BEGIN
  IF (:new.mstat = 'm' AND ABS(:new.nchild - :old.nchild) > 1)
  THEN RAISE_APPLICATION_ERROR(-20000, 'new_nchild - old_nchild must be <1');
  END IF;
END;

-- 4. Создать триггер, который отменяет любые действия (начисление, изменение, удаление) с премиями (таблица `bonus`) для неработающих в настоящий момент в организации сотрудников и сообщает об ошибке.
CREATE OR REPLACE TRIGGER bonus_trigger_task4
BEFORE INSERT OR UPDATE OR DELETE ON bonus
FOR EACH ROW
DECLARE
  careers INTEGER;
BEGIN
  SELECT COUNT(*) into careers FROM career
  WHERE empno = :new.empno and enddate IS NULL;

  IF careers = 0
  THEN RAISE_APPLICATION_ERROR(-20000, 'this employe dosnt work anymore');
  END IF;
END;

-- 5. Создайте триггер, который до выполнения действия (вставка, обновление, удаление) с таблицей `job` создаёт запись в таблице `temp_table`, с указанием названия действия (`delete`, `update`, `insert`) активизирующего триггер.
CREATE OR REPLACE TRIGGER job_trigger_task5
BEFORE INSERT OR UPDATE OR DELETE ON job
FOR EACH ROW
BEGIN
  IF INSERTING
  THEN INSERT INTO temp_table VALUES('insert');
  END IF;

  IF UPDATING
  THEN INSERT INTO temp_table VALUES('update');
  END IF;

  IF DELETING
  THEN INSERT INTO temp_table values('delete');
  END IF;
END;
