#!/usr/bin/python3
"""
This script deletes State objects with a name containing the letter 'a'
from the database 'hbtn_0e_6_usa'.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connect to the MySQL database and delete State objects with 'a'
    """
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract MySQL credentials and database name
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the connection string
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database),
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query to retrieve State objects with 'a' in the name
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Delete the State objects
    for state in states_to_delete:
        session.delete(state)

    session.commit()
    print("State objects with 'a' in the name deleted successfully.")

    # Close the session
    session.close()
