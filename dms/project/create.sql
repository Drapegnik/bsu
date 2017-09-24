DROP TABLE users;
DROP TABLE tournaments;
DROP TABLE games;
DROP TABLE tournament_systems;
DROP TABLE tournament_payments;
DROP TABLE membership_fees;
DROP TABLE game_debutes;
DROP TABLE discounts;
DROP TABLE user_discounts_mapper;

CREATE TABLE users (
    id NUMBER PRIMARY KEY,
    first_name VARCHAR2(200) NOT NULL,
    middle_name VARCHAR2(200) NOT NULL,
    last_name VARCHAR2(200) NOT NULL,
    rank NUMBER NOT NULL,
    birth_date DATE NOT NULL,
    entry_date DATE NOT NULL
);

CREATE TABLE tournaments (
    id NUMBER NOT NULL PRIMARY KEY,
    name VARCHAR2(200) NOT NULL UNIQUE,
    price NUMBER,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    system_id NUMBER NOT NULL
);

CREATE TABLE games (
    id NUMBER PRIMARY KEY,
    game_date DATE NOT NULL,
    result VARCHAR2(10) NOT NULL,
    turns_count NUMBER NOT NULL,
    white_player_id NUMBER NOT NULL,
    black_player_id NUMBER NOT NULL,
    debute_id NUMBER NOT NULL,
    tournament_id NUMBER NOT NULL,
    CONSTRAINT result_check CHECK (result in ('black', 'white', 'draw')) ENABLE
);

CREATE TABLE tournament_systems (
    id NUMBER NOT NULL PRIMARY KEY,
    name VARCHAR2(200) NOT NULL UNIQUE
);

CREATE TABLE tournament_payments (
    id NUMBER NOT NULL PRIMARY KEY,
    created_at DATE NOT NULL,
    user_id NUMBER NOT NULL,
    tournament_id NUMBER NOT NULL
);

CREATE TABLE membership_fees (
    id NUMBER NOT NULL PRIMARY KEY,
    created_at DATE NOT NULL,
    user_id NUMBER NOT NULL,
    amount NUMBER
);

CREATE TABLE game_debutes (
    id NUMBER NOT NULL PRIMARY KEY,
    name VARCHAR2(200) NOT NULL UNIQUE
);

CREATE TABLE discounts (
    id NUMBER NOT NULL PRIMARY KEY,
    name VARCHAR2(200) NOT NULL UNIQUE,
    type VARCHAR2(20) NOT NULL,
    amount NUMBER,
    CONSTRAINT type_check CHECK (type in ('percent', 'value')) ENABLE
);

CREATE TABLE user_discounts_mapper (
    id NUMBER NOT NULL PRIMARY KEY,
    user_id NUMBER NOT NULL,
    discount_id NUMBER NOT NULL,
    CONSTRAINT unique_discount UNIQUE (user_id, discount_id)
);
