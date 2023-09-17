#!/usr/bin/python3
"""
This script changes the name of a State object
in the database 'hbtn_0e_6_usa'.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connect to the MySQL database and change the name of a State object.
    """
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract MySQL credentials and database name
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the connection string
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
            .format(username, password, database),
            pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query to retrieve the State with id = 2
    state = session.query(State).filter(State.id == 2).first()

    # Change the name to "New Mexico"
    if state:
        state.name = "New Mexico"
        session.commit()
        print("Name updated successfully for State with id = 2")
    else:
        print("State with id = 2 not found")

    # Close the session
    session.close()
