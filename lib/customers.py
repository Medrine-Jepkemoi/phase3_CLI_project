from models import Category, Customer, OrderItem, Product, faker, session_maker

# from orderitem import orderitems

customers = [
    Customer(customer_fname = faker.first_name(), customer_lname = faker.last_name(), customer_mobile = '0765890766'),
    Customer(customer_fname = faker.first_name(), customer_lname = faker.last_name(), customer_mobile = '0765890766')
]



# creating customers
def create_customer():
    with session_maker() as session:
        for customer in customers:
            session.add(customer)
        session.commit()


# create_customer()

# reading customer details
def read_customers():
    with session_maker() as session:
        customers = session.query(Customer)

        for customer in customers:
            print(customer)

# read_customers()

# Validate customer

def customer_login(customer_id):
    with session_maker() as session:
        customer = session.query(Customer).filter(Customer.customer_id == customer_id).first()
        # for customer in customers:
        if customer is None:
            print("Create an account")
            return False
        else:
            print("Proceed to shop")
            return True

# customer_login(2)

# Making an order
def make_order(product_id, quantity, customer_id):
    with session_maker() as session:
        customer = session.query(Customer).filter_by(customer_id=customer_id).first()
        if customer is None:
            print("Invalid customer ID.")
            return
        else:
        
            # Check if the product exists
            product = session.query(Product).filter_by(product_id = product_id).first()
            if product is None:
                print("Product not found.")
                return
            elif product.product_amount < quantity:
                # Check if the product is available in sufficient quantity
                print("Insufficient product quantity.") 
                return
            else:
                # Create a new order item
                # orderitems = []
                order_item = OrderItem(product_id=product_id, quantity=quantity, totalprice=product.product_price * quantity, customer_id = customer_id)
                # orderitems.append(order_item)
                product.product_amount -= quantity
                session.add(order_item)
                session.commit()
                print("Order placed successfully.") 

# make_order(1, 41, 2)

def view_productscustomer():
    with session_maker() as session:
        products = session.query(Product)
        all_products = []
        # print(all_products)
        for product in products:
            category = session.query(Category).get(product.category_id)
            product_info = {
                "Product ID": product.product_id,
                "Product": product.product_name,
                "Category": category.category_name,
                "Description": product.product_description,
                "Price": product.product_price,
                "Available Units": product.product_amount
            }
            all_products.append(product_info)
        for product_info in all_products:
            print(product_info)
# view_productscustomer()

# # Deleting an order item
# def remove_orderitem(orderitem_id):
#     with session_maker() as session:
#         orderitem = session.query(OrderItem).filter_by(orderitem_id = orderitem_id).first()
#         for orderitem in orderitems:
#             session.delete(orderitem)
#         session.commit()
# remove_orderitem(3)

