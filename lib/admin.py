from models import Admin, Product, session_maker
from product import products

admins =  Admin(admin_fname = "Medrine", admin_lname = "Jepkemoi"),

# Creating an admin
with session_maker() as session:
    for admin in admins:
        session.add(admin)
    session.commit()

# function to check if admin is valid. There can only be one admin

# Admin adding product amount
def add_stock(product_id, quantity):
    with session_maker() as session:
        product = session.query(Product).get(product_id)
        product.product_amount += quantity
        session.commit()

# add_stock(1, 2)

# Admin updating product price
def update_price(product_id, price):
    with session_maker() as session:
        product = session.query(Product).get(product_id)
        product.product_price = price
        session.commit()

# update_price(1, 15)

def add_product(name, description, price, amount, category, admin):
    with session_maker() as session:
        product = session.query(Product)
        product = Product(product_name = name, product_description = description, product_price = price, product_amount = amount, category_id = category, admin_id = admin)
        session.add(product)
        session.commit()

# add_product("Apple", "This is a fruit rich in iron", 30, 100, 1, 1)

def view_products():
    with session_maker() as session:
        product = session.query(Product).all
        for product in products:
            print(product)
        session.commit()
# view_products()

def delete_product(product_id):
    with session_maker() as session:
        product = session.query(Product).filter(Product.product_id == product_id).first()
        session.delete(product)
        session.commit()
delete_product(2)
