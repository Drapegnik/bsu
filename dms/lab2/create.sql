DROP TABLE tmp_emp;
DROP TABLE tmp_job;
DROP TABLE tmp_dept;

CREATE TABLE tmp_emp (
  empno INTEGER NOT NULL,
  empname VARCHAR(15) NOT NULL,
  birthdate DATE NOT NULL
);
ALTER TABLE tmp_emp ADD PRIMARY KEY (empno);

CREATE TABLE tmp_job (
  jobno INTEGER NOT NULL,
  jobname VARCHAR(20) NOT NULL,
  minsalary REAL NOT NULL
);
ALTER TABLE tmp_job ADD PRIMARY KEY (jobno);

CREATE TABLE tmp_dept (
  deptid VARCHAR(3) NOT NULL, 
  deptname VARCHAR(20) NOT NULL, 
  deptaddress VARCHAR(25) NOT NULL
);
ALTER TABLE tmp_dept ADD PRIMARY KEY (deptid);

COMMIT;
