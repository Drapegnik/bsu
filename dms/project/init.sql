INSERT INTO users VALUES (1, 'Wilhelm', null, 'Steinitz', 2826, to_date('17-05-1836', 'dd-mm-yyyy'), to_date('17-05-1840', 'dd-mm-yyyy'));
INSERT INTO users VALUES (2, 'Emanuel', null, 'Lasker', 2878, to_date('24-12-1868', 'dd-mm-yyyy'), to_date('24-12-1872', 'dd-mm-yyyy'));
INSERT INTO users VALUES (3, 'José', 'Raúl', 'Capablanca', 2877, to_date('6-11-1888', 'dd-mm-yyyy'), to_date('6-11-1892', 'dd-mm-yyyy'));
INSERT INTO users VALUES (4, 'Aleksandr', 'Aleksandrovich', 'Alekhin', 2860, to_date('31-10-1892', 'dd-mm-yyyy'), to_date('31-10-1896', 'dd-mm-yyyy'));
INSERT INTO users VALUES (5, 'Machgielis', null, 'Euwe', 2769, to_date('20-05-1963', 'dd-mm-yyyy'), to_date('20-05-1967', 'dd-mm-yyyy'));
COMMIT;

BEGIN
    FOR i IN 1..5 LOOP
    		INSERT INTO membership_fees VALUES (i, to_date('01-01-1900', 'dd-mm-yyyy'), i, i*1000);
    END LOOP;
    COMMIT;
END;

/

INSERT INTO tournament_systems VALUES (1, 'Single Elimination');
INSERT INTO tournament_systems VALUES (2, 'Double Elimination');
INSERT INTO tournament_systems VALUES (3, 'Round');
COMMIT;

INSERT INTO tournaments VALUES (1, 'World Chess Championship #1', null, to_date('02-01-1886', 'dd-mm-yyyy'), to_date('01-01-1894', 'dd-mm-yyyy'), 1);
COMMIT;

BEGIN
    FOR i IN 1..5 LOOP
    		INSERT INTO tournament_payments VALUES (i, to_date('01-01-1886', 'dd-mm-yyyy'), i, 1);
    END LOOP;
    COMMIT;
END;

/

INSERT INTO game_debutes VALUES (1, 'Vienna Game');
INSERT INTO game_debutes VALUES (2, 'Lopez Opening');
INSERT INTO game_debutes VALUES (3, 'Danish Gambit');
INSERT INTO game_debutes VALUES (4, 'Hungarian Defense');
INSERT INTO game_debutes VALUES (5, 'Napoleon Opening');

COMMIT;

INSERT INTO games VALUES (1, to_date('15-03-1894', 'dd-mm-yyyy'), 'white', 120, 1, 2, 3, 1);
INSERT INTO games VALUES (2, to_date('16-03-1894', 'dd-mm-yyyy'), 'black', 120, 2, 1, 1, 1);
INSERT INTO games VALUES (3, to_date('17-03-1894', 'dd-mm-yyyy'), 'draw', 120, 1, 2, 4, 1);

COMMIT;

INSERT INTO discounts VALUES (1, '10% discount', 'percent', 10);
INSERT INTO discounts VALUES (2, '$100 discount', 'value', 100);

COMMIT;

INSERT INTO user_discounts_mapper VALUES (1, 1, 1);
INSERT INTO user_discounts_mapper VALUES (2, 2, 2);
INSERT INTO user_discounts_mapper VALUES (3, 1, 2);
INSERT INTO user_discounts_mapper VALUES (4, 3, 2);

COMMIT;
