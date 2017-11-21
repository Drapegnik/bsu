--------------------- USERS ---------------------

INSERT INTO users VALUES (1, 'Wilhelm', null, 'Steinitz', 2826, to_date('17-05-1836', 'dd-mm-yyyy'), to_date('17-05-1840', 'dd-mm-yyyy'));
INSERT INTO users VALUES (2, 'Emanuel', null, 'Lasker', 2878, to_date('24-12-1868', 'dd-mm-yyyy'), to_date('24-12-1872', 'dd-mm-yyyy'));
INSERT INTO users VALUES (3, 'José', 'Raúl', 'Capablanca', 2877, to_date('6-11-1888', 'dd-mm-yyyy'), to_date('6-11-1892', 'dd-mm-yyyy'));
INSERT INTO users VALUES (4, 'Aleksandr', 'Aleksandrovich', 'Alekhin', 2860, to_date('31-10-1892', 'dd-mm-yyyy'), to_date('31-10-1896', 'dd-mm-yyyy'));
INSERT INTO users VALUES (5, 'Machgielis', null, 'Euwe', 2769, to_date('20-05-1963', 'dd-mm-yyyy'), to_date('20-05-1967', 'dd-mm-yyyy'));
INSERT INTO users VALUES (6, 'Ivan', null, 'Sidorov', 590, to_date('03-11-1982', 'dd-mm-yyyy'), to_date('01-01-2016', 'dd-mm-yyyy'));
INSERT INTO users VALUES (7, 'Oleg', null, 'Bistrov', 687, to_date('21-04-1983', 'dd-mm-yyyy'), to_date('01-01-2016', 'dd-mm-yyyy'));
INSERT INTO users VALUES (8, 'Ivan', null, 'Ivanov', 978, to_date('14-03-1997', 'dd-mm-yyyy'), to_date('01-01-2017', 'dd-mm-yyyy'));
INSERT INTO users VALUES (9, 'Petr', null, 'Petrov', 1021, to_date('29-05-1996', 'dd-mm-yyyy'), to_date('01-01-2017', 'dd-mm-yyyy'));
COMMIT;

--------------------- MEMBERSHIP FEES ---------------------

BEGIN
    FOR i IN 1..5 LOOP
    		INSERT INTO membership_fees VALUES (i, to_date('01-01-1900', 'dd-mm-yyyy'), i, i*1000);
    END LOOP;
    COMMIT;
END;

/

INSERT INTO membership_fees VALUES (6, to_date('01-01-2016', 'dd-mm-yyyy'), 6, 500);
INSERT INTO membership_fees VALUES (7, to_date('01-01-2016', 'dd-mm-yyyy'), 7, 500);
INSERT INTO membership_fees VALUES (8, to_date('01-01-2017', 'dd-mm-yyyy'), 8, 500);
INSERT INTO membership_fees VALUES (9, to_date('01-01-2017', 'dd-mm-yyyy'), 9, 500);

--------------------- TOURNAMENT SYSTEMS ---------------------

INSERT INTO tournament_systems VALUES (1, 'Single Elimination');
INSERT INTO tournament_systems VALUES (2, 'Double Elimination');
INSERT INTO tournament_systems VALUES (3, 'Round');
COMMIT;

--------------------- TOURNAMENTS ---------------------

INSERT INTO tournaments VALUES (1, 'World Chess Championship #1', null, to_date('02-01-1886', 'dd-mm-yyyy'), to_date('01-01-1894', 'dd-mm-yyyy'), 1);
INSERT INTO tournaments VALUES (2, '2016 Major', 100, to_date('01-02-2016', 'dd-mm-yyyy'), to_date('01-03-2016', 'dd-mm-yyyy'), 1);
INSERT INTO tournaments VALUES (3, '2017 Major', 150, to_date('01-02-2017', 'dd-mm-yyyy'), to_date('01-03-2017', 'dd-mm-yyyy'), 1);
INSERT INTO tournaments VALUES (4, '2017 Summer Camp', 50, to_date('01-06-2017', 'dd-mm-yyyy'), to_date('01-09-2017', 'dd-mm-yyyy'), 3);
COMMIT;

--------------------- TOURNAMENT PAYMENTS ---------------------
-- tournament 1
BEGIN
    FOR i IN 1..5 LOOP
    		INSERT INTO tournament_payments VALUES (i, to_date('01-01-1886', 'dd-mm-yyyy'), i, 1);
    END LOOP;
    COMMIT;
END;

/

-- tournament 2
INSERT INTO tournament_payments VALUES (6, to_date('01-02-2016', 'dd-mm-yyyy'), 6, 2);
INSERT INTO tournament_payments VALUES (7, to_date('01-02-2016', 'dd-mm-yyyy'), 7, 2);

-- tournament 3
INSERT INTO tournament_payments VALUES (8, to_date('01-02-2017', 'dd-mm-yyyy'), 6, 3);
INSERT INTO tournament_payments VALUES (9, to_date('01-02-2017', 'dd-mm-yyyy'), 7, 3);
INSERT INTO tournament_payments VALUES (10, to_date('01-02-2017', 'dd-mm-yyyy'), 8, 3);
INSERT INTO tournament_payments VALUES (11, to_date('01-02-2017', 'dd-mm-yyyy'), 9, 3);

-- tournament 4
INSERT INTO tournament_payments VALUES (12, to_date('01-06-2017', 'dd-mm-yyyy'), 6, 4);
INSERT INTO tournament_payments VALUES (13, to_date('01-06-2017', 'dd-mm-yyyy'), 7, 4);
INSERT INTO tournament_payments VALUES (14, to_date('01-06-2017', 'dd-mm-yyyy'), 8, 4);
INSERT INTO tournament_payments VALUES (15, to_date('01-06-2017', 'dd-mm-yyyy'), 9, 4);

--------------------- GAME DEBUTES ---------------------

INSERT INTO game_debutes VALUES (1, 'Vienna Game');
INSERT INTO game_debutes VALUES (2, 'Lopez Opening');
INSERT INTO game_debutes VALUES (3, 'Danish Gambit');
INSERT INTO game_debutes VALUES (4, 'Hungarian Defense');
INSERT INTO game_debutes VALUES (5, 'Napoleon Opening');

COMMIT;

--------------------- GAMES ---------------------
-- tournament 1
INSERT INTO games VALUES (1, to_date('15-03-1894', 'dd-mm-yyyy'), 'white', 120, 1, 2, 3, 1);
INSERT INTO games VALUES (2, to_date('16-03-1894', 'dd-mm-yyyy'), 'black', 120, 2, 1, 1, 1);
INSERT INTO games VALUES (3, to_date('17-03-1894', 'dd-mm-yyyy'), 'draw', 120, 1, 2, 4, 1);

-- tournament 2
INSERT INTO games VALUES (4, to_date('03-02-2016', 'dd-mm-yyyy'), 'white', 5, 6, 7, 1, 2);

-- tournament 3
INSERT INTO games VALUES (5, to_date('03-02-2017', 'dd-mm-yyyy'), 'black', 5, 6, 7, 4, 3);
INSERT INTO games VALUES (6, to_date('04-02-2017', 'dd-mm-yyyy'), 'white', 29, 8, 9, 2, 3);
INSERT INTO games VALUES (7, to_date('05-02-2017', 'dd-mm-yyyy'), 'black', 79, 7, 8, 1, 3);

-- tournament 4
INSERT INTO games VALUES (8, to_date('03-06-2017', 'dd-mm-yyyy'), 'white', 8, 6, 8, 4, 4);
INSERT INTO games VALUES (9, to_date('04-06-2017', 'dd-mm-yyyy'), 'white', 90, 7, 9, 2, 4);
INSERT INTO games VALUES (10, to_date('05-06-2017', 'dd-mm-yyyy'), 'white', 153, 6, 7, 1, 4);

COMMIT;

--------------------- DISCOUNTS ---------------------

INSERT INTO discounts VALUES (1, '10% discount', 'percent', 10);
INSERT INTO discounts VALUES (2, '$100 discount', 'value', 100);

COMMIT;

--------------------- UDW ---------------------

INSERT INTO user_discounts_mapper VALUES (1, 1, 1);
INSERT INTO user_discounts_mapper VALUES (2, 2, 2);
INSERT INTO user_discounts_mapper VALUES (3, 1, 2);
INSERT INTO user_discounts_mapper VALUES (4, 3, 2);

COMMIT;
