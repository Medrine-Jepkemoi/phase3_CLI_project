from models import Customer, faker, session_maker

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

read_customers()




