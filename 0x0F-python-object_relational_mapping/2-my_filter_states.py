#!/usr/bin/python3
"""
This script connects to a MySQL database and displays all values in the states
table where the name matches the provided state name.
"""

import sys
import MySQLdb


def filter_states_by_name(username, password, database, state_name):
    """
    Connects to the MySQL server and filters states by the provided state name.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the database.
        state_name (str): State name to search for.

    Returns:
        None
    """
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=database)
        cursor = db.cursor()

        # Create the SQL query using the provided state name
        sql_query = "SELECT * FROM states WHERE name LIKE '{}' ORDER BY id".format(state_name)

        # Execute the query
        cursor.execute(sql_query)

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
    Main function that takes MySQL username, password, database name, and state
    name as arguments and calls the filter_states_by_name function.
    """
    # Check if correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get the command-line arguments
    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Call the function to filter states by name
    filter_states_by_name(username, password, database, state_name)
