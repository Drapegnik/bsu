-- 1. Имеется `PL/SQL`-блок, содержащий следующие операторы:
--    ```sql
--    DECLARE
--         empnum INTEGER;
--    BEGIN
--        INSERT INTO BONUS VALUES (505, 15, 2012, 500, NULL);
--        INSERT INTO JOB VALUES (1010, 'Accountant xxxxxxxxxx', 5500);
--        SELECT empno INTO empnum FROM EMP WHERE empno=505 OR empno=403;
--    END;
--    ```
--    * Каждый из операторов исполняемого раздела вызывает предопределённое исключение со своими предопределёнными кодом и сообщением.
--    * Дополните блок разделом обработки исключительных ситуаций.
--    * Обработка каждой ситуации состоит в занесении в таблицу `T_ERROR` предопределённых кода ошибки, сообщения об ошибке и текущих даты и времени, когда ошибка произошла.
DECLARE
  emp_num INTEGER;
  error_code INTEGER;
  error_message VARCHAR(100);
BEGIN
  INSERT INTO BONUS VALUES (505, 15, 2012, 500, NULL);
  INSERT INTO JOB VALUES (1010, 'Accountant xxxxxxxxxx', 5500);
  SELECT empno INTO emp_num FROM EMP
  WHERE empno = 505 OR empno = 403;

  EXCEPTION WHEN OTHERS THEN error_code := SQLCODE;
    error_message := SUBSTR(SQLERRM, 1, 100);
    INSERT INTO T_ERROR VALUES (error_code, error_message, SYSDATE);
END;

/* OUTPUT
ERR_NUM  ERR_MSG                                                                                   ERR_TIME
-------- ----------------------------------------------------------------------------------------  ---------
   -2290 ORA-02290: check constraint (SYSTEM.SYS_C0020328) violated                                04-DEC-17
  -12899 ORA-12899: value too large for column "SYSTEM"."JOB"."JOBNAME" (actual: 21, maximum: 20)  04-DEC-17
   -1422 ORA-01422: exact fetch returns more than requested number of rows                         04-DEC-17
*/

-- 2. Создайте собственную исключительную ситуацию с кодом `-20000` и сообщением `January bonus greater February bonus` или `February bonus greater March bonus` в зависимости от месяца, данные за который вызвали ситуацию.
--    * Исключительная ситуация наступает при нарушении бизнес-правила:
--      > Сумма премий, начисленных в конкретном месяце `2017` года, не может быть меньше суммы премий, начисленных в предыдущий месяц этого же года.
--    * Таким образом рассматриваются только январь, февраль и март `2017` года.
--    * Внесите операторы, определяющие нарушение бизнес-правила и обработку соответсвующей ситуации в блок.
--    * При наступлении пользователской исключительной ситуации обработка состоит в занесении данных о ней (аналогично пункту 1) в таблицу `T_ERROR`.
DECLARE
  CURSOR total_bonus_by_month (year INTEGER) IS
  SELECT MONTH, SUM(bonvalue) AS bonvalue FROM bonus
  WHERE YEAR = year GROUP BY MONTH ORDER BY MONTH;

  prev_month_bonus REAL := 0;
  prev_moth INTEGER := 0;
  prev_moth_name VARCHAR(20);
  curr_month_name VARCHAR(20);
  error_code INTEGER;
  error_message VARCHAR(100);
BEGIN
  FOR i IN total_bonus_by_month(2017)
    LOOP
      IF ((prev_moth = i.month - 1) AND (prev_month_bonus > i.bonvalue)) THEN
        SELECT TO_CHAR(TO_DATE(i.month - 1, 'MM'), 'MONTH')
        INTO prev_moth_name FROM DUAL;

        SELECT TO_CHAR(TO_DATE(i.month, 'MM'), 'MONTH')
        INTO curr_month_name FROM DUAL;

        RAISE_APPLICATION_ERROR(-20000, prev_moth_name || 'bonus greater ' || curr_month_name || 'bonus');
      END IF;

      prev_month_bonus := i.bonvalue;
      prev_moth := i.month;
    END LOOP;

    EXCEPTION WHEN OTHERS THEN error_code := SQLCODE;
      error_message := SUBSTR(SQLERRM, 1, 100);
      INSERT INTO T_ERROR VALUES (error_code, error_message, SYSDATE);
END;

/* OUTPUT
ERR_NUM     ERR_MSG                                           ERR_TIME
----------  -----------------------------------------------   ---------
 -20000     ORA-20000: JANUARY  bonus greater FEBRUARY bonus  04-DEC-17
*/
