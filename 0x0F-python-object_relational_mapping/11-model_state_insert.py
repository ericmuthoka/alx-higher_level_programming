#!/usr/bin/python3
"""
This script adds the State object "Louisiana" to the database 'hbtn_0e_6_usa'.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connect to the MySQL database and add the State object "Louisiana".
    """
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the connection string
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Create a new State object for Louisiana
    louisiana_state = State(name="Louisiana")

    # Add the State object to the session
    session.add(louisiana_state)
    session.commit()

    # Display the new states.id
    print(louisiana_state.id)

    # Close the session
    session.close()
