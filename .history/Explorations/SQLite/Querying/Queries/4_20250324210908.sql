SELECT
	"first_name",
	"last_name"
FROM
	"players"
WHERE
	"birth_country" <> 'USA'
ORDER BY
	"first_name" ASC,
	"last_name" ASC;

SELECT
	"first_name",
	"last_name",
	"debut"
FROM
	"players"
WHERE
	"birth_city" = 'Pittsburgh'
	AND "birth_state" = 'PA'
ORDER BY
	"debut" DESC,
	"first_name" ASC,
	"last_name" ASC



SELECT
	COUNT(*)
FROM
	"players"
WHERE
	(
		"bats" = 'L'
		AND "throws" = 'R'
	)
	OR (
		"bats" = 'R'
		AND "throws" = 'L'
	);


SELECT
	ROUND(AVG("height"), 2) AS "Average Height",
	ROUND(AVG("weight"), 2) AS "Average Weight"
FROM
	"players"
WHERE
	"debut" > '2000-01-01';

SELECT
	"first_name",
	"last_name"
FROM
	"players"
WHERE
	"final_game" BETWEEN '2022-01-01' AND '2022-12-31'
ORDER BY
	"first_name" ASC,
	"last_name" ASC;


SELECT
	"first_name" AS "USA Players"
FROM
	"players"
WHERE
	"birth_country" = 'USA'
ORDER BY
	'first_name';
