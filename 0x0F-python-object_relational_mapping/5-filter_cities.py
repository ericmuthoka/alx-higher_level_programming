#!/usr/bin/python3
"""
Lists cities of a specified state from 'hbtn_0e_4_usa' database.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    Connect to MySQL and retrieve cities of the specified state.
    """
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=database)
        cursor = db.cursor()

        # Prepare a safe SQL query using a prepared statement
        query = ("SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') "
                 "FROM cities "
                 "JOIN states ON cities.state_id = states.id "
                 "WHERE states.name = %s "
                 "ORDER BY cities.id")
        cursor.execute(query, (state_name,))

        # Fetch the result and display it
        result = cursor.fetchone()
        if result:
            print(result[0])

        # Close cursor and database connection
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("Error: Unable to connect to MySQL server:", str(e))
