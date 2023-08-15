-- Creates a table called second_table in the database hbtn_0c_0 and adds multiple rows.
CREATE TABLE IF NOT EXISTS hbtn_0c_0.second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Insert multiple rows into the second_table.
INSERT INTO hbtn_0c_0.second_table (id, name, score) VALUES
    (1, 'Alice', 95),
    (2, 'Bob', 87),
    (3, 'Charlie', 78),
    (4, 'David', 92),
    (5, 'Eve', 89);
