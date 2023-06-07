# from customers import orderitems
from models import OrderItem, Product, faker, session_maker

# orderitems = [
#     OrderItem(product_id = 1, quantity = 2, totalprice = 10, customer_id = 2),
#     OrderItem(product_id = 1, quantity = 4, totalprice = 35, customer_id = 1)

# ]

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

def delete_order(orderitem_id):
    with session_maker() as session:
        orderitem = session.query(OrderItem).filter(OrderItem.orderitem_id == orderitem_id).first()
        session.delete(orderitem)
        session.commit()

# delete_order(1)

# Customer functions on orders
#  View customer order

def customer_order(customer_id):
    with session_maker() as session:

        orderitems = session.query(OrderItem).filter(OrderItem.customer_id == customer_id).all()
        # print(orderitem)
        if len(orderitems) == 0 :
            print("Customer has no orders")
        else:
            order_details = []
            for orderitem in orderitems:
                product = session.query(Product).get(orderitem.product_id)
                order_details.append(
                    f"Product: {product.product_name}, Quantity:{orderitem.quantity}, Total Price: {orderitem.totalprice}"
                )        
                print(order_details)
# customer_order(2)


# Customer updating order item
def update_orderitem(orderitem_id, quantity):
    with session_maker() as session:
        orderitem = session.query(OrderItem).filter_by(orderitem_id = orderitem_id).first()
        orderitem.quantity += quantity
        print("Order item updated successfully")
        session.commit()
update_orderitem(1, 5)



# Customer deleting an order item
def remove_orderitem(orderitem_id):
    with session_maker() as session:
        orderitem = session.query(OrderItem).filter_by(orderitem_id = orderitem_id).first()
        session.delete(orderitem)
        print("Order item deleted successfully")
        session.commit()

# remove_orderitem(4)
