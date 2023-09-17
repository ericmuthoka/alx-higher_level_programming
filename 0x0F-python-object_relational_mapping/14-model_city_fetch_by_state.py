#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa.
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
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

    # Query to retrieve City objects
    cities = session.query(City).order_by(City.id).all()

    # Print City objects with their corresponding State names
    for city in cities:
        state_name = session.query(State).filter_by(id=city.state_id).first().name
        print("{}: ({}) {}".format(state_name, city.id, city.name))

    # Close the session
    session.close()
