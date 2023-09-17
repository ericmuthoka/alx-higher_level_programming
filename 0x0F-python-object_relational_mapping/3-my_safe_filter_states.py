#!/usr/bin/python3
"""
This script connects to a MySQL database and displays states from the 'states'
table that match the provided state name, using a safe method to prevent SQL
injection.
"""

import sys
import MySQLdb


if __name__ == "__main__":
    """
    Connect to the MySQL database and retrieve states that match the provided
    state name using a safe method to prevent SQL injection.
    """
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cursor = db.cursor()

        # Create a safe SQL query using a prepared statement
        query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id"
        state_name = (sys.argv[4],)

        # Execute the query with the safe parameter
        cursor.execute(query, state_name)

        # Fetch all the results and display them
        results = cursor.fetchall()
        for row in results:
            print(row)

        # Close the cursor and the database connection
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("Error: Unable to connect to the MySQL server:", str(e))
