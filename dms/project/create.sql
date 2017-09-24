DROP TABLE user_discounts_mapper;
DROP TABLE discounts;
DROP TABLE tournament_payments;
DROP TABLE membership_fees;
DROP TABLE games;
DROP TABLE game_debutes;
DROP TABLE tournaments;
DROP TABLE tournament_systems;
DROP TABLE users;

CREATE TABLE users (
    id NUMBER PRIMARY KEY,
    first_name VARCHAR2(200) NOT NULL,
    middle_name VARCHAR2(200),
    last_name VARCHAR2(200) NOT NULL,
    rank NUMBER NOT NULL,
    birth_date DATE NOT NULL,
    entry_date DATE NOT NULL
);

CREATE TABLE tournament_systems (
    id NUMBER NOT NULL PRIMARY KEY,
    name VARCHAR2(200) NOT NULL UNIQUE
);

CREATE TABLE tournaments (
    id NUMBER NOT NULL PRIMARY KEY,
    name VARCHAR2(200) NOT NULL UNIQUE,
    price NUMBER,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    system_id NUMBER NOT NULL,

    CONSTRAINT tournaments_fk_system
        FOREIGN KEY (system_id)
        REFERENCES tournament_systems(id)
);

CREATE TABLE game_debutes (
    id NUMBER NOT NULL PRIMARY KEY,
    name VARCHAR2(200) NOT NULL UNIQUE
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
    
    CONSTRAINT result_check CHECK (result in ('black', 'white', 'draw')) ENABLE,
    CONSTRAINT games_fk_debute
        FOREIGN KEY (debute_id)
        REFERENCES game_debutes(id),
    CONSTRAINT games_fk_white_player
        FOREIGN KEY (white_player_id)
        REFERENCES users(id),    
    CONSTRAINT games_fk_black_player
        FOREIGN KEY (black_player_id)
        REFERENCES users(id),
    CONSTRAINT games_fk_tournament
        FOREIGN KEY (tournament_id)
        REFERENCES tournaments(id)
);

CREATE TABLE tournament_payments (
    id NUMBER NOT NULL PRIMARY KEY,
    created_at DATE NOT NULL,
    user_id NUMBER NOT NULL,
    tournament_id NUMBER NOT NULL,

    CONSTRAINT tp_fk_user
        FOREIGN KEY (user_id)
        REFERENCES users(id),
    CONSTRAINT tp_fk_tournament
        FOREIGN KEY (tournament_id)
        REFERENCES tournaments(id)
);

CREATE TABLE membership_fees (
    id NUMBER NOT NULL PRIMARY KEY,
    created_at DATE NOT NULL,
    user_id NUMBER NOT NULL,
    amount NUMBER,

    CONSTRAINT membership_fees_fk_user
        FOREIGN KEY (user_id)
        REFERENCES users(id)
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

    CONSTRAINT udm_unique_discount UNIQUE (user_id, discount_id),
    CONSTRAINT user_discounts_mapper_fk_user
        FOREIGN KEY (user_id)
        REFERENCES users(id),
    CONSTRAINT udm_fk_discount
        FOREIGN KEY (discount_id)
        REFERENCES discounts(id)
);
