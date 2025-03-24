
-- SELECT * FROM "publishers";

-- SELECT "id" FROM "publishers" WHERE "publisher" = 'MacLehose Press'; 
-- 12
-- SELECT "title" FROM "books" WHERE "publisher_id" = 12;

-- SELECT "title" FROM "books" WHERE "publisher_id" = (
--     SELECT "id" FROM "publishers" WHERE "publisher" = 'MacLehose Press');

-- Find all ratings for this book called in memory of memory

-- How to find all features of "rating" table
-- SELECT * FROM "translated";

-- SELECT "rating" FROM "ratings" WHERE "book_id" = (
--     SELECT "id" FROM "books" WHERE "title" = 'In Memory of Memory');

-- SELECT AVG("rating") FROM "ratings" WHERE "book_id" = (
--     SELECT "id" FROM "books" WHERE "title" = 'In Memory of Memory');

-- MANY to MANY

-- Find the author how wrote Flights

-- SELECT "name" FROM "authors" 
-- WHERE "id" = (
--     SELECT "author_id" FROM "authored" WHERE "book_id"=(
--         SELECT "id" FROM "books" WHERE "title" = 'Flights'));

-- Find all books written by "Fernanda Melchor"

-- SELECT "title" FROM "books" 
-- WHERE "id" IN (
--     SELECT "book_id" FROM "authored" 
--     WHERE "author_id" = (
--         SELECT "id" FROM "authors" 
--         WHERE "name" = 'Fernanda Melchor'
--         )
--     );



-- -- Books without a translator
-- SELECT "title", "translator" FROM "longlist" WHERE "translator" IS NULL;

-- -- Books with a translator
-- SELECT "title", "translator" FROM "longlist" WHERE "translator" IS NOT NULL;

-- Find all books with "love" in the title
SELECT "title" FROM "longlist" WHERE "title" LIKE '%love%';

-- Find all books that begin with "The" (includes "There", etc.)
SELECT "title" FROM "longlist" WHERE "title" LIKE 'The%';

-- Find all books that begin with "The"
SELECT "title" FROM "longlist" WHERE "title" LIKE 'The %';

-- Find a book whose title unsure how to spell
SELECT "title" FROM "longlist" WHERE "title" LIKE 'P_re';

-- Top 10 books by rating (incorrectly)
SELECT "title", "rating" FROM "longlist" ORDER BY "rating" LIMIT 10;

-- Top 10 books by rating (correctly)
SELECT "title", "rating" FROM "longlist" ORDER BY "rating" DESC LIMIT 10;

-- Ordering by more than one column
SELECT "title", "rating", "votes" FROM "longlist" 
ORDER BY "rating" DESC, "votes" DESC
LIMIT 10;

-- Ordering with a condition
SELECT "title", "rating" FROM "longlist" 
WHERE "votes" > 10000 ORDER BY "rating" DESC 
LIMIT 10;


-- Find the average rating of all longlisted books
SELECT AVG("rating") FROM "longlist";

-- Round the result
SELECT ROUND(AVG("rating"), 2) FROM "longlist";

-- Rename column with AS
SELECT ROUND(AVG("rating"), 2) AS "Average Rating" FROM "longlist";

-- Find maximum rating
SELECT MAX("rating") FROM "longlist";

-- Find minimum rating
SELECT MIN("rating") FROM "longlist";

-- Find total number of votes
SELECT SUM("votes") FROM "longlist";

-- Find total number of books
SELECT COUNT(*) FROM "longlist";

-- Find total number of translators
SELECT COUNT("translator") FROM "longlist";

-- Incorrectly count publishers
SELECT COUNT("publisher") FROM "longlist";

-- Correctly count publishers
SELECT COUNT(DISTINCT "publisher") FROM "longlist";