
from admin import (add_product, add_stock, delete_product, update_price,
                   view_productsadmin)
from customers import customer_login, make_order, view_productscustomer
from orderitem import customer_order, remove_orderitem, update_orderitem


def main():

    choice = 0
    while choice != 3:
        print("*** TUTTI FRUITY ONLINE GREENGROCERY")
        print("1) Enter system as an customer")
        print("2) Enter system as a administrator") 
        print("3) Exit system")

        choice = int(input())

        if choice == 1:
            # enter system as a customer
            customer_id = input("Enter your id: ")
            customer_login(customer_id)

            customer_choice = 0
            while customer_choice != 6:

                print("*** Customer's View")
                print("1) View products")
                print("2) Make an order")
                print("3) View orders")
                print("4) Update order item")
                print("5) Delete order item")
                print("6) Go back to main menu")

                customer_choice = int(input())

                if customer_choice == 1:
                    view_productscustomer()
                elif customer_choice == 2:
                    product_id = input("Enter the product ID: ")
                    quantity = int(input("Enter the product quantity: "))
                    customer_id = input("Enter your id: ")
                    make_order(product_id, quantity, customer_id)
                elif customer_choice == 3:
                    customer_id = input("Enter your id: ")
                    customer_order(customer_id)
                elif customer_choice == 4:
                    orderitem_id = input("Enter the order item ID: ")
                    quantity = int(input("Enter the product quantity: "))
                    update_orderitem(orderitem_id, quantity)
                elif customer_choice == 5:
                    orderitem_id = input("Enter the order item ID: ")
                    remove_orderitem(orderitem_id)
            
        if choice == 2:

            admin_choice = 0
            while admin_choice != 6:
            
                print("*** Admin's View")
                print("1) View products")
                print("2) Add products")
                print("3) Update stock")
                print("4) Update price")
                print("5) Delete product")
                print("6) Go back to main menu")

                admin_choice =int(input())

                if admin_choice == 1:
                    view_productsadmin()

                elif admin_choice == 2:
                    product_name = input("Enter the name of the product: ")
                    product_description = input("Enter the description of the product: ")
                    product_price = input("Enter the price of the product: ")
                    product_amount = input("Enter the amount of the product: ")
                    category_id = input("Enter the category of the product: ")
                    admin_id = input("Enter the your ID: ")


                    add_product(product_name, product_description, product_price, product_amount, category_id, admin_id)

                elif admin_choice == 3:
                    product_id = input("Enter the ID of the product: ")
                    quantity = int(input("Enter the quantity: "))
                    add_stock(product_id, quantity)

                elif admin_choice == 4:
                    product_id = input("Enter the ID of the product: ")
                    price = int(input("Enter the price: "))
                    update_price(product_id, price)
                     
                elif admin_choice == 5:
                    product_id = input("Enter id of product you want to delete: ")
                    delete_product(product_id)




                
                    

        # elif choice == 2:
        #     # enter system as an administrator





if __name__ == "__main__":
    main()
