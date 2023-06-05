from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# creating the engine / database
engine = create_engine('sqlite:///grocery.db')

# Creating the tables
Base = declarative_base()

# Customer table
class Customer(Base):
    __tablename__ = 'customers'
    customer_id = Column(Integer, primary_key = True)
    customer_fname = Column(String)
    customer_lname = Column(String)
    customer_location = Column(String)
    customer_mobile = Column(String)


# Admin table
class Admin(Base):
    __tablename__ = 'admins'
    admin_id = Column(Integer, primary_key = True)
    admin_fname = Column(String)
    admin_lname = Column(String)

class Grocery(Base):
    __tablename__ = 'groceries'
    grocery_id = Column(Integer, primary_key = True)
    grocery_name = Column(String)
    grocery_location = Column(String)

class Categories(Base):
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key = True)
    category_name = Column(String)

class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key = True)
    product_name = Column(String)
    product_price = Column(Integer)
    product_amount = Column(Integer)

class Order(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key = True)
    order_amount = Column(Integer)


Base.metadata.create_all(engine)
