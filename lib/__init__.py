from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


# creating the engine / database
engine = create_engine('sqlite:///grocery.db')
Base.metadata.create_all(engine)
