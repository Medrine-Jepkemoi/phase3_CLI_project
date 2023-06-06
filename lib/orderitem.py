from models import OrderItem, faker, session_maker

orderitems = [
    OrderItem(product_id = 1, quantity = 2, totalprice = 10, customer_id = 2),
    OrderItem(product_id = 1, quantity = 4, totalprice = 35, customer_id = 1)

]

# creating products
def create_order():
    with session_maker() as session:
        for orderitem in orderitems:
            session.add(orderitem)
        session.commit()

# create_order()

def view_order():
    with session_maker() as session:
        orderitems = session.query(OrderItem)
        for orderitem in orderitems:
            print(orderitem)

# view_order()

def update_order():
    with session_maker() as session:
        orderitem = session.query(OrderItem).filter(OrderItem.orderitem_id == 2).first()
        orderitem.quantity = 8
        session.commit()

# update_order()

def delete_order():
    with session_maker() as session:
        orderitem = session.query(OrderItem).filter(OrderItem.orderitem_id == 2).first()
        session.delete(orderitem)
        session.commit()

delete_order()
