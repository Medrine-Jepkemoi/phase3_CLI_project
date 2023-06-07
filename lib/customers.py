from models import Customer, OrderItem, Product, faker, session_maker

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

# def customer_login(self, customer_id):
#     with session_maker() as session:
#         customer = session.query(Customer).filter(Customer.customer_id == customer_id).all()
#         for customer in customers:
#             if customer in customers:
#                 print("Customer exists")
#             else:
#                 print("Sign up")

# # customer_login( 3)

# # Customer ordering
# def customer_order(self, product_id, quantity):
#     session = session_maker()
#     product = session.query(Product).filter_by(product_id=product_id).first()

#     if product is None:
#         session.close()
#         return "Invalid product ID. Order placement failed."

#     if product.product_amount < quantity:
#         session.close()
#         return "Insufficient product quantity. Order placement failed."

#     total_price = product.product_price * quantity

#     order_item = OrderItem(product_id=product_id, quantity=quantity, totalprice=total_price, customer_id=self.customer_id)
#     session.add(order_item)
#     session.commit()
#     session.close()

#     return "Order placed successfully."

# # Usage example:
# customer_id = 1  # Example customer ID
# product_id = 1  # Example product ID
# quantity = 2

# with session_maker() as session:
#     customer = session.query(Customer).filter_by(customer_id=customer_id).first()
#     if customer is None:
#         print("Invalid customer ID.")
#     else:
#         result = customer.customer_order(product_id, quantity)
#         print(result)



