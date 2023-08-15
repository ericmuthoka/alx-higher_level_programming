-- Create a table named second_table with columns id, name, and score in the MySQL server.
CREATE TABLE IF NOT EXISTS `second_table` (
    `id` INT,
    `name` VARCHAR(256),
    `score` INT
);

-- Insert multiple rows into the second_table.
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES
    (1, "John", 10),
    (2, "Alex", 3),
    (3, "Bob", 14),
    (4, "George", 8);

-- Retrieve and display the data from the second_table.
SELECT * FROM `second_table`;

