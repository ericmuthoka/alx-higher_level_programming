-- a script that creates the table force_name on MySQL server.
USE your_database_name;  -- Replace with the actual database name

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

