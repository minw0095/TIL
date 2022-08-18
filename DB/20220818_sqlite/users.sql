create table users(
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

.mode csv

.import users.csv users