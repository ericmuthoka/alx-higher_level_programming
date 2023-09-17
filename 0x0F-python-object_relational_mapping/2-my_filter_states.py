#!/usr/bin/python3
"""
This script takes a state name as an argument and displays all values in the
'states' table where the 'name' matches the provided state name from the
'hbtn_0e_0_usa' database.
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """
    Connect to the MySQL database and retrieve the states
    where the 'name' matches the provided state name.
    """
    db_connection = db.connect(host="localhost", port=3306,
            user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connection.cursor()

    query = (
            "SELECT * FROM states WHERE name LIKE BINARY '{}' "
            "ORDER BY states.id ASC"
            .format(argv[4])
            )
    db_cursor.execute(query)

    selected_rows = db_cursor.fetchall()

    for row in selected_rows:
        print(row)
