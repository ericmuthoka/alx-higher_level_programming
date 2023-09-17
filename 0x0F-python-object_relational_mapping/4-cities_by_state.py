#!/usr/bin/python3
"""
This script lists all cities from the database 'hbtn_0e_4_usa'.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    Connect to the MySQL database and retrieve all cities sorted by their IDs.
    """
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cursor = db.cursor()

        # Execute the query to select all cities and join with states
        cursor.execute("SELECT cities.id, cities.name, states.name "
                       "FROM cities "
                       "JOIN states ON cities.state_id = states.id "
                       "ORDER BY cities.id")

        # Fetch all the results and display them
        results = cursor.fetchall()
        for row in results:
            print(row)

        # Close the cursor and the database connection
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("Error: Unable to connect to the MySQL server:", str(e))
