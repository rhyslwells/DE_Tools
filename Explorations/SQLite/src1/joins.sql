-- Demonstrates joining tables with JOIN
-- Uses sea_lions.db

-- Shows all sea lions for which we have data
SELECT * FROM "sea_lions"
JOIN "migrations" ON "migrations"."id" = "sea_lions"."id";

-- Shows all sea lions, whether or not we have data
SELECT * FROM "sea_lions"
LEFT JOIN "migrations" ON "migrations"."id" = "sea_lions"."id";

-- Shows all data, whether or not there are matching sea lions
SELECT * FROM "sea_lions"
RIGHT JOIN "migrations" ON "migrations"."id" = "sea_lions"."id";

-- Shows all data and all sea lions
SELECT * FROM "sea_lions"
FULL JOIN "migrations" ON "migrations"."id" = "sea_lions"."id";

-- JOINs sea lions and migrations without specifying matching column
SELECT * FROM "sea_lions"
NATURAL JOIN "migrations";

-- Uses WHERE after joining a table
SELECT * FROM "sea_lions"
JOIN "migrations" ON "migrations"."id" = "sea_lions"."id"
WHERE "migrations"."distance" > 1500;
