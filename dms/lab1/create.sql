DROP TABLE BONUS;
DROP TABLE CAREER;
DROP TABLE EMP;
DROP TABLE DEPT;
DROP TABLE JOB;

/******************************************************/
/*          Departments (Подразделения)               */ 
/******************************************************/
CREATE TABLE dept (
	deptid VARCHAR (3) PRIMARY KEY NOT NULL, 
	deptname VARCHAR (20) NOT NULL, 
	deptaddress VARCHAR(25) NOT NULL
);
COMMIT;

INSERT INTO dept VALUES ('B02', 'Support', 'Belarus, Minsk') ;
INSERT INTO dept VALUES ('U03', 'Development', 'USA, San-Diego'); 
INSERT INTO dept VALUES ('B01', 'Administration', 'Belarus, Minsk') ;
INSERT INTO dept VALUES ('U01', 'Administration', 'USA, San-Diego'); 
INSERT INTO dept VALUES ('C02', 'Web-technology', 'Czechia,  Praga');
INSERT INTO dept VALUES ('B03', 'Personnel management', 'Belarus,  Minsk');
INSERT INTO dept VALUES ('U02', 'Research', 'USA, Dallas');
INSERT INTO dept VALUES ('C01', 'Accounting', 'Czechia, Praga');
INSERT INTO dept VALUES ('B04', 'Sales', 'Belarus, Minsk');
INSERT INTO dept VALUES ('U04', 'Operations', 'USA, Boston');
INSERT INTO dept VALUES ('B05', 'Production', 'Belarus, Minsk');
COMMIT;

/******************************************************/
/*          Employers (Работники)                     */ 
/******************************************************/
CREATE TABLE emp (
	empno INTEGER PRIMARY KEY NOT NULL, 
	empname VARCHAR (15) NOT NULL, 
	birthdate DATE NOT NULL CHECK (birthdate > to_date('01-01-1954','dd-mm-yyyy'))
);
COMMIT;

INSERT INTO emp VALUES (101, 'Steve Bobrowski', to_date('02-04-1983','dd-mm-yyyy')); 
INSERT INTO emp VALUES (102, 'Don Burleson', to_date('10-06-1973','dd-mm-yyyy')); 
INSERT INTO emp VALUES (103, 'Vera Rovdo', to_date('03.09.1980','dd-mm-yyyy'));
INSERT INTO emp VALUES (104, 'Olga Buben', to_date('23.11.1982','dd-mm-yyyy')) ; 
INSERT INTO emp VALUES (105, 'Mark Gokman', to_date('21.11.1978','dd-mm-yyyy')) ;
INSERT INTO emp VALUES (201, 'Jon Ingmar', to_date('14.01.1980','dd-mm-yyyy')) ;
INSERT INTO emp VALUES (203, 'Irina Klimovich', to_date('25.07.1982','dd-mm-yyyy'));
INSERT INTO emp VALUES (204, 'Svetlana Brich', to_date('17.11.1985','dd-mm-yyyy'));
INSERT INTO emp VALUES (205, 'Larisa Usich', to_date('19.02.1975','dd-mm-yyyy'));
INSERT INTO emp VALUES (209, 'Kevin Loney', to_date('06.08.1977','dd-mm-yyyy'));
INSERT INTO emp VALUES (211, 'Grady Booch', to_date('23.05.1977','dd-mm-yyyy'));
INSERT INTO emp VALUES (215, 'Frank Boumphrey', to_date('12.10.1979','dd-mm-yyyy'));
INSERT INTO emp VALUES (303, 'Nina Tihanovich',to_date('05.08.1976','dd-mm-yyyy'));
INSERT INTO emp VALUES (304, 'Pavel Zuck', to_date('25.11.1981','dd-mm-yyyy')); 
INSERT INTO emp VALUES (311, 'Olivia Direnzo', to_date('13.03.1970','dd-mm-yyyy')); 
INSERT INTO emp VALUES (321, 'Jon Duckett', to_date('19.09.1971','dd-mm-yyyy')) ;
INSERT INTO emp VALUES (322, 'Dave Hollander', to_date('13.05.1972','dd-mm-yyyy')) ; 
INSERT INTO emp VALUES (327, 'Trevor Jenkins', to_date('21.02.1972','dd-mm-yyyy')); 
INSERT INTO emp VALUES (329, 'Peter Jones', to_date('19.01.1982','dd-mm-yyyy'));
INSERT INTO emp VALUES (401, 'Craig McQueen', to_date('29.12.1960','dd-mm-yyyy')); 
INSERT INTO emp VALUES (402, 'Stephen Mohr', to_date('25.05.1965','dd-mm-yyyy'));  
INSERT INTO emp VALUES (403, 'Jon Martin', to_date('15.07.1955','dd-mm-yyyy')) ;  
INSERT INTO emp VALUES (404, 'Richard Martin', to_date('23.02.1960','dd-mm-yyyy'));
INSERT INTO emp VALUES (410, 'Robert Grishuk', to_date('15.07.1965','dd-mm-yyyy')); 
INSERT INTO emp VALUES (412, 'Vladimir Liss', to_date('18.10.1965','dd-mm-yyyy'));
INSERT INTO emp VALUES (414, 'Piter Mohov', to_date('25.12.1976','dd-mm-yyyy')) ;
INSERT INTO emp VALUES (503, 'Alex Kuznetsov', to_date('14.09.1980','dd-mm-yyyy'));
INSERT INTO emp VALUES (504, 'Ivan Dudin', to_date('25.03.1981','dd-mm-yyyy')) ;
INSERT INTO emp VALUES (505, 'Fedor Dikunov', to_date('12.07.1965','dd-mm-yyyy'));
INSERT INTO emp VALUES (601, 'Anna Zlotnik', to_date('18.05.1979','dd-mm-yyyy'));  
COMMIT;

/******************************************************/
/*          Jobs (Должности)                          */ 
/******************************************************/
CREATE TABLE job (
	jobno INTEGER PRIMARY KEY NOT NULL, 
	jobname VARCHAR(20) NOT NULL, 
	minsalary REAL NOT NULL
);
COMMIT;

INSERT INTO job VALUES (1000, 'Manager', 2500);
INSERT INTO job VALUES (1001, 'Financial Director', 7500);
INSERT INTO job VALUES (1003, 'Salesman', 1500);
INSERT INTO job VALUES (1002, 'Executive Director', 8000);
INSERT INTO job VALUES (1004, 'Clerk', 500);
INSERT INTO job VALUES (1005, 'Driver', 1800);
INSERT INTO job VALUES (1006, 'President', 15000);
INSERT INTO job VALUES (1007, 'Engineer', 7000);
INSERT INTO job VALUES (1008, 'Programmer', 7500);
INSERT INTO job VALUES (1009, 'Accountant',5500);
COMMIT;

/******************************************************/
/*          Career (Служебная карьера)                */ 
/******************************************************/
CREATE TABLE career (
	jobno INTEGER REFERENCES job(jobno) NOT NULL, 
	empno INTEGER REFERENCES emp(empno) NOT NULL,
	deptid VARCHAR(3) REFERENCES dept(deptid) NOT NULL,
	startdate DATE NOT NULL, 
	enddate DATE, 
	CHECK (startdate < enddate)
);
COMMIT;

INSERT INTO career VALUES  (1008, 101, 'U03', to_date('01.05.2015','dd-mm-yyyy'), null);
INSERT INTO career VALUES  (1002, 102, 'U01', to_date('01.01.2007','dd-mm-yyyy'), to_date('31.12.2012','dd-mm-yyyy'));
INSERT INTO career VALUES  (1006, 102, 'U01', to_date('01.01.2013','dd-mm-yyyy'), null);
INSERT INTO career VALUES  (1008, 103, 'B02', to_date('01.01.2016','dd-mm-yyyy'), null);
INSERT INTO career VALUES  (1008, 104, 'B02', to_date('01.09.2016','dd-mm-yyyy'), null);
INSERT INTO career VALUES  (1007, 105, 'U04', to_date('01.09.2016','dd-mm-yyyy'), to_date('31.03.2017','dd-mm-yyyy'));
INSERT INTO career VALUES  (1008, 201, 'U02', to_date('01.06.2016','dd-mm-yyyy'), to_date('31.03.2017','dd-mm-yyyy'));
INSERT INTO career VALUES  (1008, 203, 'U02', to_date('01.10.2013','dd-mm-yyyy'), to_date('31.03.2016','dd-mm-yyyy'));
INSERT INTO career VALUES  (1007, 203, 'B05', to_date('01.07.2016','dd-mm-yyyy'), null);
INSERT INTO career VALUES  (1007, 204, 'U02', to_date('01.06.2014','dd-mm-yyyy'), to_date('31.12.2016','dd-mm-yyyy'));
INSERT INTO career VALUES  (1007, 204, 'B02', to_date('01.04.2017','dd-mm-yyyy'), null);
INSERT INTO career VALUES  (1008, 205, 'B02', to_date('01.10.2015','dd-mm-yyyy'), to_date('31.12.2016','dd-mm-yyyy'));
INSERT INTO career VALUES  (1008, 205, 'C01', to_date('01.02.2017','dd-mm-yyyy'), null);
INSERT INTO career VALUES  (1004, 209, 'U01', to_date('01.01.2015','dd-mm-yyyy'), to_date('31.01.2017','dd-mm-yyyy'));
INSERT INTO career VALUES  (1008, 211, 'U03', to_date('01.04.2016','dd-mm-yyyy'), null);
INSERT INTO career VALUES  (1004, 215, 'U04', to_date('01.06.2014','dd-mm-yyyy'), to_date('31.03.2016','dd-mm-yyyy'));
INSERT INTO career VALUES  (1004, 215, 'U03', to_date('01.04.2016','dd-mm-yyyy'), null);
INSERT INTO career VALUES  (1009, 303, 'B01', to_date('01.01.2012','dd-mm-yyyy'), to_date('31.12.2015','dd-mm-yyyy'));
INSERT INTO career VALUES  (1001, 303, 'B01', to_date('01.02.2016','dd-mm-yyyy'), null);
INSERT INTO career VALUES  (1000, 304, 'B04', to_date('01.01.2016','dd-mm-yyyy'), to_date('31.12.2016','dd-mm-yyyy'));
INSERT INTO career VALUES  (1004, 311, 'U04', to_date('01.06.2014','dd-mm-yyyy'), to_date('31.03.2016','dd-mm-yyyy'));
INSERT INTO career VALUES  (1007, 321, 'U03', to_date('01.09.2012','dd-mm-yyyy'), to_date('31.12.2016','dd-mm-yyyy'));
INSERT INTO career VALUES  (1008, 322, 'U02', to_date('01.09.2012','dd-mm-yyyy'), to_date('31.12.2016','dd-mm-yyyy'));
INSERT INTO career VALUES  (1007, 322, 'U03', to_date('01.02.2017','dd-mm-yyyy'), null);
INSERT INTO career VALUES  (1009, 327, 'U01', to_date('01.01.2014','dd-mm-yyyy'), null);
INSERT INTO career VALUES  (1008, 329, 'U02', to_date('01.04.2014','dd-mm-yyyy'), to_date('31.05.2016','dd-mm-yyyy'));
INSERT INTO career VALUES  (1008, 329, 'U02', to_date('01.09.2017','dd-mm-yyyy'), null);
INSERT INTO career VALUES  (1009, 401, 'C01', to_date('01.09.2005','dd-mm-yyyy'), null);
INSERT INTO career VALUES  (1002, 402, 'C02', to_date('01.02.2009','dd-mm-yyyy'), null);
INSERT INTO career VALUES  (1008, 403, 'C02', to_date('01.09.2012','dd-mm-yyyy'), null);
INSERT INTO career VALUES  (1001, 404, 'C01', to_date('01.01.2012','dd-mm-yyyy'), to_date('31.12.2015','dd-mm-yyyy'));
INSERT INTO career VALUES  (1002, 404, 'U01', to_date('01.02.2016','dd-mm-yyyy'), null);
INSERT INTO career VALUES  (1007, 410, 'B05', to_date('01.10.2010','dd-mm-yyyy'), to_date('31.03.2014','dd-mm-yyyy'));
INSERT INTO career VALUES  (1007, 410, 'B02', to_date('01.09.2014','dd-mm-yyyy'), to_date('31.05.2016','dd-mm-yyyy'));
INSERT INTO career VALUES  (1007, 410, 'B02', to_date('01.09.2016','dd-mm-yyyy'), to_date('31.05.2017','dd-mm-yyyy'));
INSERT INTO career VALUES  (1002, 412, 'B02', to_date('01.02.2013','dd-mm-yyyy'), to_date('30.04.2015','dd-mm-yyyy'));
INSERT INTO career VALUES  (1002, 412, 'B05', to_date('01.05.2015','dd-mm-yyyy'), to_date('31.12.2016','dd-mm-yyyy'));
INSERT INTO career VALUES  (1002, 412, 'B02', to_date('01.02.2017','dd-mm-yyyy'), null);
INSERT INTO career VALUES  (1008, 414, 'B02', to_date('01.04.2013','dd-mm-yyyy'), to_date('31.12.2016','dd-mm-yyyy'));
INSERT INTO career VALUES  (1008, 503, 'B02', to_date('01.04.2016','dd-mm-yyyy'), null);
INSERT INTO career VALUES  (1005, 504, 'B04', to_date('01.05.2012','dd-mm-yyyy'), to_date('30.08.2013','dd-mm-yyyy'));
INSERT INTO career VALUES  (1005, 504, 'B05', to_date('01.01.2014','dd-mm-yyyy'), to_date('30.04.2016','dd-mm-yyyy'));
INSERT INTO career VALUES  (1005, 504, 'B05', to_date('01.01.2017','dd-mm-yyyy'), null);
INSERT INTO career VALUES  (1006, 505, 'B01', to_date('01.06.2007','dd-mm-yyyy'), null);
INSERT INTO career VALUES  (1007, 601, 'B05', to_date('01.07.2013','dd-mm-yyyy'), null);
COMMIT;

/******************************************************/
/*         Bonus (Премия)                             */ 
/******************************************************/
CREATE TABLE bonus (
	empno INTEGER REFERENCES emp(empno) NOT NULL,
	month SMALLINT CHECK (month > 0 and month < 13),
	year INTEGER CHECK (year > 2012 and year < 2018),
	bonvalue REAL
);
COMMIT;

INSERT INTO bonus VALUES (505, 1, 2013, 500);
INSERT INTO bonus VALUES (505, 2, 2013, 500);
INSERT INTO bonus VALUES (404, 3, 2013, 300);
INSERT INTO bonus VALUES (404, 5, 2013, 300);
INSERT INTO bonus VALUES (102, 4, 2013, 300);
INSERT INTO bonus VALUES (102, 5, 2013, 300);
INSERT INTO bonus VALUES (102, 9, 2013, 1000);
INSERT INTO bonus VALUES (303, 6, 2013, 300);
INSERT INTO bonus VALUES (504, 7, 2013, 100);
INSERT INTO bonus VALUES (412, 3, 2013, 400);
INSERT INTO bonus VALUES (412, 8, 2013, 400);
INSERT INTO bonus VALUES (412,12, 2013, 400);
INSERT INTO bonus VALUES (601, 9, 2013, 200);
INSERT INTO bonus VALUES (601,12, 2013, 200);
INSERT INTO bonus VALUES (414,10, 2013, 350);
INSERT INTO bonus VALUES (321,11, 2013, 350);
INSERT INTO bonus VALUES (322,12, 2013, 350);
INSERT INTO bonus VALUES (401,12, 2013, 350);
/****************************/
INSERT INTO bonus VALUES (102, 1, 2014, 500);
INSERT INTO bonus VALUES (505, 2, 2014, 500);
INSERT INTO bonus VALUES (102, 3, 2014, 500);
INSERT INTO bonus VALUES (404, 4, 2014, 300);
INSERT INTO bonus VALUES (504, 5, 2014, 150);
INSERT INTO bonus VALUES (412, 6, 2014, 300);
INSERT INTO bonus VALUES (601, 7, 2014, 250);
INSERT INTO bonus VALUES (321, 8, 2014, 300);
INSERT INTO bonus VALUES (322, 9, 2014, 300);
INSERT INTO bonus VALUES (403,10, 2014, 400);
INSERT INTO bonus VALUES (402,11, 2014, 450);
INSERT INTO bonus VALUES (403,12, 2014, 200);
/*****************************/
INSERT INTO bonus VALUES (505, 1, 2015, 500);
INSERT INTO bonus VALUES (102, 2, 2015, 500);
INSERT INTO bonus VALUES (329, 3, 2015, 400);
INSERT INTO bonus VALUES (401, 4, 2015, 300);
INSERT INTO bonus VALUES (402, 5, 2015, 400);
INSERT INTO bonus VALUES (403, 6, 2015, 350);
INSERT INTO bonus VALUES (329, 7, 2015, 400);
INSERT INTO bonus VALUES (403, 7, 2015, 400);
INSERT INTO bonus VALUES (327, 7, 2015, 250);
INSERT INTO bonus VALUES (303, 8, 2015, 450);
INSERT INTO bonus VALUES (101, 9, 2015, 350);
INSERT INTO bonus VALUES (504,10, 2015, 150);
INSERT INTO bonus VALUES (401,11, 2015, 200);
INSERT INTO bonus VALUES (303,12, 2015, 350);
/*************************/
INSERT INTO bonus VALUES (505, 1, 2016, 500);
INSERT INTO bonus VALUES (102, 1, 2016, 500);
INSERT INTO bonus VALUES (322, 2, 2016, 350);
INSERT INTO bonus VALUES (321, 2, 2016, 350);
INSERT INTO bonus VALUES (103, 2, 2016, 350);
INSERT INTO bonus VALUES (211, 3, 2016, 350);
INSERT INTO bonus VALUES (329, 4, 2016, 350);
INSERT INTO bonus VALUES (503, 5, 2016, 350);
INSERT INTO bonus VALUES (414, 6, 2016, 300);
INSERT INTO bonus VALUES (211, 7, 2016, 300);
INSERT INTO bonus VALUES (503, 8, 2016, 350);
INSERT INTO bonus VALUES (203, 9, 2016, 300);
INSERT INTO bonus VALUES (211,10, 2016, 300);
INSERT INTO bonus VALUES (401,11, 2016, 300);
INSERT INTO bonus VALUES (403,12, 2016, 350);
INSERT INTO bonus VALUES (101,12, 2016, 350);
/*************************/
INSERT INTO bonus VALUES (505, 1, 2017, 500);
INSERT INTO bonus VALUES (102, 1, 2017, 500);
INSERT INTO bonus VALUES (102, 2, 2017, 500);
INSERT INTO bonus VALUES (401, 3, 2017, 600);
INSERT INTO bonus VALUES (402, 3, 2017, 600);
INSERT INTO bonus VALUES (403, 4, 2017, 700);
INSERT INTO bonus VALUES (104, 5, 2017, 500);
INSERT INTO bonus VALUES (103, 6, 2017, 500);
INSERT INTO bonus VALUES (102, 6, 2017, 500);
INSERT INTO bonus VALUES (203, 7, 2017, 500);
INSERT INTO bonus VALUES (205, 8, 2017, 300);
COMMIT;
