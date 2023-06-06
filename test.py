from sqlalchemy import create_engine

Base = declarative_base()


# creating the engine / database
engine = create_engine('sqlite:///grocery.db')
