-- Demonstrates removing a table
-- Uses mbta.db

-- Removes riders table
DROP TABLE "riders";

-- Demonstrates renaming a table
-- Uses mbta.db

-- Renames "vists" table to "swipes"
ALTER TABLE "visits" RENAME TO "swipes";


-- Demonstrates adding a column to a table
-- Uses mbta.db

-- Adds "ttpe" column to "swipes" table (intentional typo)
ALTER TABLE "swipes" ADD COLUMN "ttpe" TEXT;


-- Demonstrates renaming a column
-- Uses mbta.db

-- Fixes typo using RENAME COLUMN
ALTER TABLE "swipes" RENAME COLUMN "ttpe" TO "type";
