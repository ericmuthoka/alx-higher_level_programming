#!/usr/bin/python3
"""
This script connects to a MySQL database and displays states from the 'states'
table that match the provided state name.
"""

import sys
import MySQLdb


if __name__ == "__main__":
    """
    Connect to the MySQL database and retrieve states that match the provided
    state name.
    """
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cursor = db.cursor()

        # Create the SQL query using the provided state name
        query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id"\
                .format(sys.argv[4])

        # Execute the query
        cursor.execute(query)

        # Fetch all the results and display them
        results = cursor.fetchall()
        for row in results:
            print(row)

        # Close the cursor and the database connection
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("Error: Unable to connect to the MySQL server:", str(e))
