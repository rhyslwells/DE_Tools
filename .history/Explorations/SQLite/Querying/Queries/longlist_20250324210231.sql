
-- .tables

SELECT * FROM "publishers";

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



