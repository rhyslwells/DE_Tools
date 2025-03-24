-- how to join two tables using primary keys

-- .tables

-- SELECT * FROM "sea_lions";

-- SELECT * FROM "migrations";

SELECT * FROM "sea_lions" 
JOIN "migrations" on "migrations"."id" = "sea_lions"."id"; 

-- SELECT * FROM "migrations";

-- SELECT * FROM "sea_lions" 
-- LEFT JOIN "migrations" on "migrations"."id" = "sea_lions"."id"; 

-- SELECT * FROM "sea_lions" 
-- RIGHT JOIN "migrations" on "migrations"."id" = "sea_lions"."id"; 

-- SELECT * FROM "sea_lions"
-- FULL JOIN "migrations" on "migrations"."id" = "sea_lions"."id";

-- natural identification of ids
SELECT * FROM "sea_lions"
NATURAL JOIN "migrations";


