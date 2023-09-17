#!/usr/bin/python3
"""
This script prints the states.id for a given state name from the
database 'hbtn_0e_6_usa'.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connect to the MySQL database and retrieve the states.id for
    the given state name.
    """
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Create the connection string
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query to retrieve the states.id for the given state name
    state = session.query(State).filter(State.name == state_name).first()

    # Display the result or "Not found" if state not found
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
