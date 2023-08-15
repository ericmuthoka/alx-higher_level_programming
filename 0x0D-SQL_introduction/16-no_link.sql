-- a script that lists all records of the table second_table of the database hbtn_0c_0
-- Descending order
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
