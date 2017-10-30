--1. Найти сведения обо всех партиях, сыгранных конкретным шахматистом (имя игрока – параметр запроса);
SELECT 
  game_date, white_player_id, black_player_id, result, debute_id, turns_count, tournament_id 
FROM users
JOIN games ON (
  white_player_id = users.id OR black_player_id = users.id
)
WHERE first_name = 'Wilhelm' AND last_name = 'Steinitz';

--2. Найти сведения обо всех шахматистах, не плативших членские взносы в течение текущего года;
SELECT * FROM users
WHERE users.id NOT IN (
  SELECT users.id FROM users
  JOIN membership_fees ON user_id = users.id
  WHERE created_at >= ADD_MONTHS(CURRENT_DATE, -12)
);

--3. Найти сведения о двух самых старых шахматистах, игравших в турнирах текущего года. Включить в результат запроса сумму денег, выигранную ими на этих турнирах;
SELECT * FROM (
  SELECT DISTINCT users.id, first_name, last_name, birth_date FROM users 
  JOIN games ON (
    white_player_id = users.id OR black_player_id = users.id
  )
  WHERE (game_date >= ADD_MONTHS(CURRENT_DATE, -12))
)
WHERE ROWNUM < 3
ORDER BY birth_date;