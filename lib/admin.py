from models import Admin, Category, Product, session_maker

# from product import products

admins =  Admin(admin_fname = "Medrine", admin_lname = "Jepkemoi"),

# # Creating an admin
# with session_maker() as session:
#     for admin in admins:
#         session.add(admin)
#     session.commit()

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
        print("Product added successfully!")
        session.commit()

# add_product("Chicken thighs", "Excellent source of iron and zinc ", 50, 600, 4, 1)

# Admin viewing products
def view_productsadmin():
    with session_maker() as session:
        products = session.query(Product)
        all_products = []
        # print(all_products)
        for product in products:
            category = session.query(Category).get(product.category_id)
            all_products.append(
                f"Product ID: {product.product_id}, Product: {product.product_name}, Description: {product.product_description}, Price: {product.product_price}, Available Units: {product.product_amount}, Category ID: {product.category_id}, Category: {category.category_name} "
            )
            print(all_products)
        session.commit()
# view_productsadmin()

def delete_product(product_id):
    with session_maker() as session:
        product = session.query(Product).filter(Product.product_id == product_id).first()
        session.delete(product)
        session.commit()
# delete_product(2)
