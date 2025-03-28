CREATE TABLE "movies" (
    "id" INTEGER,
    "title" TEXT NOT NULL,
    "year" NUMERIC,
    PRIMARY KEY("id")
);

CREATE TABLE "people" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "birth" NUMERIC,
    PRIMARY KEY("id")
);

CREATE TABLE "ratings" (
    "id" INTEGER,
    "movie_id" INTEGER UNIQUE,
    "rating" REAL NOT NULL,
    "votes" INTEGER NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY("movie_id") REFERENCES "movies"("id")
);

CREATE TABLE "stars" (
    "movie_id" INTEGER,
    "person_id" INTEGER,
    PRIMARY KEY("movie_id", "person_id"),
    FOREIGN KEY("movie_id") REFERENCES "movies"("id"),
    FOREIGN KEY("person_id") REFERENCES "people"("id")
);

