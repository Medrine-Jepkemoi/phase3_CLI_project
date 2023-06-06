from faker import Faker
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# Instantiate faker class
faker = Faker()

# Creating the tables

# Customer table
class Customer(Base):
    __tablename__ = 'customers'
    customer_id = Column(Integer, primary_key = True)
    customer_fname = Column(String)
    customer_lname = Column(String)
    customer_mobile = Column(String)
    customer_order = relationship('OrderItem', back_populates = 'order_customer')
    

# Admin table
class Admin(Base):
    __tablename__ = 'admins'
    admin_id = Column(Integer, primary_key = True)
    admin_fname = Column(String)
    admin_lname = Column(String)
    admin_product = relationship('Product', back_populates = 'product_admin')


class Category(Base):
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key = True)
    category_name = Column(String)
    category_product = relationship('Product', back_populates = 'product_category')


class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key = True)
    product_name = Column(String)
    product_description = Column(String)
    product_price = Column(Integer)
    product_amount = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    admin_id = Column(Integer, ForeignKey('admins.admin_id'))
    product_admin = relationship('Admin', back_populates = 'admin_product')
    product_category = relationship('Category', back_populates = 'category_product')


class OrderItem(Base):
    __tablename__ = 'orderitems'

    orderitem_id = Column(Integer, primary_key = True)
    product_id = Column(Integer)
    quantity = Column(Integer)
    totalprice = Column(Integer)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    order_customer = relationship('Customer', back_populates = 'customer_order')


f = Faker()
print(f.name())
# print(f.age)
