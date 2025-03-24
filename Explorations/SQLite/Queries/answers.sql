-- -- Basics
-- -- get the table name of players.db

-- -- table name
-- -- SELECT name
-- -- FROM sqlite_master
-- -- WHERE type = 'table';
-- -- table called players

-- -- how to get the columns in a table ands store as list
PRAGMA table_info(players);

-- -- In 1.sql, write a SQL query to find the hometown (including city, state, and country) of Jackie Robinson.

-- SELECT "birth_city", "birth_state", "birth_country" FROM "players" WHERE "first_name" = "Jackie" AND "last_name" = "Robinson";

-- -- In 2.sql, write a SQL query to find the side (e.g., right or left) Babe Ruth hit.

-- SELECT "bats" FROM "players" WHERE "first_name" = "Babe" AND "last_name" = "Ruth";

-- -- In 3.sql, write a SQL query to find the ids of rows for which a value in the column debut is missing.

-- SELECT "id" FROM "players" WHERE "debut" IS NULL;


-- -- In 4.sql, write a SQL query to find the first and last names of players who were not born in the United States. Sort the results alphabetically by first name, then by last name.

-- SELECT "first_name", "last_name" FROM "players" WHERE "birth_country" != "USA" ORDER BY "first_name", "last_name";

-- -- In 5.sql, write a SQL query to return the first and last names of all right-handed batters. Sort the results alphabetically by first name, then by last name.

-- SELECT "first_name", "last_name" FROM "players" WHERE "bats" = "R" ORDER BY "first_name", "last_name";

-- -- In 6.sql, write a SQL query to return the first name, last name, and debut date of players born in Pittsburgh, Pennsylvania (PA). Sort the results first by debut date—from most recent to oldest—then alphabetically by first name, followed by last name.

-- SELECT "first_name", "last_name", "debut" FROM "players" WHERE "birth_city" = "Pittsburgh" AND "birth_state" = "PA" ORDER BY "debut" DESC, "first_name", "last_name";

-- -- In 7.sql, write a SQL query to count the number of players who bat (or batted) right-handed and throw (or threw) left-handed, or vice versa.
SELECT COUNT(*) FROM "players" WHERE "bats" = "R" AND "throws" = "L";


-- In 8.sql, write a SQL query to find the average height and weight, rounded to two decimal places, of baseball players who debuted on or after January 1st, 2000. Return the columns with the name “Average Height” and “Average Weight”, respectively.


SELECT ROUND(AVG("height"), 2) AS "Average Height", ROUND(AVG("weight"), 2) AS "Average Weight" FROM "players" WHERE "debut" >= "2000-01-01";


-- In 9.sql, write a SQL query to find the players who played their final game in the MLB in 2022. Sort the results alphabetically by first name, then by last name.

-- SELECT "first_name", "last_name", "final_game", FROM "players" WHERE "final_game" IS NOT NULL ORDER BY "final_game" DESC LIMIT 10;


SELECT "first_name", "last_name", "final_game" FROM "players" WHERE "final_game" >= '2022-01-01' AND "final_game" < '2023-01-01' ORDER BY "final_game" DESC LIMIT 10;
