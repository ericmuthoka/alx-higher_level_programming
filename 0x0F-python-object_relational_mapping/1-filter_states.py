#!/usr/bin/python3
"""
This script connects to a MySQL database and lists states with names starting
with 'N' from the 'states' table in ascending order of their IDs.
"""

import sys
import MySQLdb


def list_states_with_n(username, password, database):
    """
    Connects to the MySQL server and lists states with names starting with 'N'
    from the 'states' table.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the database.

    Returns:
        None
    """
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=database)
        cursor = db.cursor()

        # Execute the query to select states with names starting with 'N'
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

        # Fetch all the results and display them
        results = cursor.fetchall()
        for row in results:
            print(row)

        # Close the cursor and the database connection
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("Error: Unable to connect to the MySQL server:", str(e))


if __name__ == "__main__":
    """
    Main function that takes MySQL username, password, and database name as
    arguments and calls the list_states_with_n function.
    """
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get the command-line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to list states starting with 'N'
    list_states_with_n(username, password, database)
