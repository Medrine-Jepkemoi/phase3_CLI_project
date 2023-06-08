from datetime import datetime

from models import Admin, Category, Customer, OrderItem, Product, session_maker

# from product import products

admins =  Admin(admin_fname = "Medrine", admin_lname = "Jepkemoi"),

# # Creating an admin
# with session_maker() as session:
#     for admin in admins:
#         session.add(admin)
#     session.commit()

# function to check if admin is valid. There can only be one admin
def is_admin(admin_id):
    with session_maker() as session:
        admin = session.query(Admin).get(admin_id)
        if admin is not None and admin.admin_id == 1:
            print("Welcome admin.")
        else:
            print("Access denied, you are not an admin!")

# is_admin(admin_id)

# Admin adding product amount
def add_stock(product_id, quantity):
    with session_maker() as session:
        product = session.query(Product).get(product_id)
        product.product_amount += quantity
        print("Product update successfully!")
        session.commit()

# add_stock(1, 2)

# Admin updating product price
def update_price(product_id, price):
    with session_maker() as session:
        product = session.query(Product).get(product_id)
        product.product_price = price
        print("Price updates successfully!")
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
            product_info = {
                "Product ID": product.product_id,
                "Product": product.product_name,
                "Description": product.product_description,
                "Price": product.product_price,
                "Available Units": product.product_amount,
                "Category ID": product.category_id,
                "Category": category.category_name
            }
            all_products.append(product_info)

        for product_info in all_products:
            print(product_info)
        session.commit()
# view_productsadmin()

def delete_product(product_id):
    with session_maker() as session:
        product = session.query(Product).filter(Product.product_id == product_id).first()
        session.delete(product)
        print("Product deleted successfullly!")
        session.commit()
# delete_product(2)



# Admin viewing the highest order amount on the current day
def highest_orderreport(date):
    with session_maker() as session:
        # Query orders made on the specified day
        orders = session.query(OrderItem).filter(OrderItem.order_date.like(f'{date}%')).all()
        
        if len(orders) == 0:
            print("No orders found on the specified day")
            return {}
        else:
            # Calculate the total price of each customer's orders
            customer_totals = {}
            for order_item in orders:
                customer_id = order_item.customer_id
                total_price = order_item.totalprice
                if customer_id in customer_totals:
                    customer_totals[customer_id] += total_price
                else:
                    customer_totals[customer_id] = total_price
            
            # Find the customer with the highest total order
            highest_customer = max(customer_totals, key=customer_totals.get)
            
            # Retrieve the customer details
            customer = session.query(Customer).get(highest_customer)
            
            # Store the report in a dictionary
            report = {
                'Customer Id': customer.customer_id,
                'Customer Name': f"{customer.customer_fname} {customer.customer_lname}",
                'Customer Mobile': customer.customer_mobile,
                'Total Order Amount': customer_totals[highest_customer]
            }
            
            print(report)
            return 


# date = datetime.now().strftime("%Y-%m-%d")
# highest_orderreport(date)

