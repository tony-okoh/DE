# Load product and courier names from .txt files
def open_file(filename):
    file = open(filename, "r")
    product = file.read()
    products = product.split()
    file.close()
    return products

products = open_file("products.txt")
couriers = open_file("couriers.txt")

#dump lists into file.txt 
def write_file(filename, items):
    try:
        file = open(filename, 'w')
        for item in items:
            file.write(item + '\n')
        file.close()
    except Exception as e:
        print('An error occurred: ' + str(e))


#main menu list
Main_Menu = ["Product Menu", "Courier", "Order", "Exit/Write to file.txt"]

#print main menu
while True:
    print("MAIN MENU\n----------\nActions\nEnter '1' for Product Menu\nEnter '2' for Courier Menu\nEnter '3' for Order Menu\nEnter '0' to Exit\n")
    Selection1 = int(input("Enter Selection: "))
#dump products and courier lists into file.txt and exit app
    if Selection1 == 0:
        write_file("products.txt", products)
        write_file("couriers.txt", couriers)
        print("Exiting Application - Goodbye!")
        break
#print products menu
    if Selection1 == 1:      
        while True:
            print("\nPRODUCTS MENU\nEnter '0' to go back to MAIN MENU\nEnter '1' for PRODUCT LIST\n"
                    "Enter '2' for NEW PRODUCT\nEnter '3' to UPDATE PRODUCT\nEnter '4' to DELETE PRODUCT \n")          
            Selection2 = (int(input("Enter Menu Selection(Number): ")))
            if Selection2 == 0:
                break
#create order list from customer input
            while True:
                if Selection2 == 1:
                    print(*products,sep='\n') 
                    break
#create new product                
                elif Selection2 == 2:
                    products.append(input("Add New product: "))   
                    print("You have added a new product\n")                 
                    print("New product list: ",products)
                    break
#update existing product                
                elif Selection2 == 3:
                    for index, value in enumerate(products):
                        print(index, value)
                    user_index = int(input("\nEnter product number: "))
                    user_value = (input("Enter product name: ")).lower()
                    print("\n")
                    products[user_index] = user_value
                    for index, value in enumerate(products):                        
                        print("Updated Product List: ",index, value)
                    break
#delete a product                
                elif Selection2 == 4:
                    for index, value in enumerate(products):
                        print(index, value)                    
                    product_index = (int(input("\nEnter product number:\n")))
                    print(f"You are deleting: {product_index} =", products.pop(product_index))
                    print("\n")
                    for index, value in enumerate(products):                        
                        print("The New Product List: ",index, value)
                    break
    if Selection1 == 2:      
        while True:
            print("\nCOURIER MENU\nEnter '0' to go back to MAIN MENU\nEnter '1' for COURIER LIST\n"
                    "Enter '2' for NEW COURIER\nEnter '3' to UPDATE COURIER\nEnter '4' to DELETE COURIER: \n")            
            Selection2 = (int(input("Enter Menu Selection(Number): ")))
            if Selection2 == 0:
                break
#create courier list from customer input                   
            while True:
                if Selection2 == 1:
                    print(*couriers,sep='\n')  
                    try:
                        n = int(input("\nHow many couriers do you wish to select? Enter Number: ")) 
                    except:
                        print("\nPlease enter NUMBER!!!")
                        break
                    courier_list = []
                    print("\nEnter courier(s) from the list:")
                    for i in range(n):				
                        courier_list.append(input().title())                   
                    check = all(item in couriers for item in courier_list)
                    if check is True:                    
                        print(f"\nThank you, please wait for {courier_list}.\n")
                        break
                    else:                        
                        print("\nI'm sorry, that courier does not exist.\n")
                        continue
#create a new courier                
                elif Selection2 == 2:
                    couriers.append(input("New courier: "))
                    print("You have added a new courier\n")
                    print("New courier list: ",couriers)
                    break
#update existing courier list                
                elif Selection2 == 3:
                    for index, value in enumerate(couriers):
                        print(index, value)
                    user_index = int(input("\nEnter courier number: "))
                    user_value = (input("Enter courier name: ")).lower()
                    print("\n")
                    couriers[user_index] = user_value
                    for index, value in enumerate(couriers):                        
                        print("Updated Courier List: ",index, value)
                    break
#delete courier                
                elif Selection2 == 4:
                    for index, value in enumerate(couriers):
                        print(index, value)                    
                    courier_index = (int(input("\nEnter courier number:\n")))
                    print(f"You are deleting: {courier_index} =", couriers.pop(courier_index))
                    print("\n")
                    for index, value in enumerate(couriers):                        
                        print("The New Courier List: ",index, value)
                    break
    if Selection1 == 3:  
#order list
        orders = {
        "customer_name:": "",
        "customer_address:": "",
        "customer_phone:": "",
        "courier:": "",
        "status:": ""
        }
        while True:
            print("\nORDER MENU\nEnter '0' to go back to MAIN MENU\nEnter '1' for ORDER LIST\n"
                    "Enter '2' for NEW ORDER\nEnter '3' to UPDATE ORDER\nEnter '4' to DELETE ORDER: \n")            
            Selection2 = (int(input("Enter Menu Selection(Number): ")))
            if Selection2 == 0:
                break
#create order list from customer input                   
            while True:
                if Selection2 == 1:
                    print(*orders, '\n')  
                    try:
                        n1 = input("\nCustomer Name: ")
                        n2 = input("\nCustomer Address: ")
                        n3 = int(input("\n\nCustomer Phone Number: ")) 
                        n4 = int(input("\nCourier: ")) 
                        n5 = (input("\nStatus: ")) 
                        
                    except:
                        print("\nPlease enter NUMBER!!!")
                        break
                    order_list = []
                    print("\nEnter order(s) from the list:")
                    for i in range(n):				
                        order_list.append(input().title())                   
                    check = all(item in orders for item in order_list)
                    if check is True:                    
                        print(f"\nThank you, please wait for {order_list}.\n")
                        break
                    else:                        
                        print("\nI'm sorry, that order does not exist.\n")
                        continue
#create a new order                
                elif Selection2 == 2:
                    orders.append(input("New order: "))
                    print("You have added a new order\n")
                    print("New courier list: ",orders)
                    break
#update existing order list                
                elif Selection2 == 3:
                    for index, value in enumerate(orders):
                        print(index, value)
                    user_index = int(input("\nEnter courier number: "))
                    user_value = (input("Enter order name: ")).lower()
                    print("\n")
                    orders[user_index] = user_value
                    for index, value in enumerate(orders):                        
                        print("Updated Order List: ",index, value)
                    break
#delete order                
                elif Selection2 == 4:
                    for index, value in enumerate(orders):
                        print(index, value)                    
                    order_index = (int(input("\nEnter order number:\n")))
                    print(f"You are deleting: {order_index} =", orders.pop(order_index))
                    print("\n")
                    for index, value in enumerate(orders):                        
                        print("The New Order List: ",index, value)
                    break










# products = ["Fries", "Burgers", "Wraps", "Salads", "Vegan", "Drinks", "Desserts", "Cakes", "Sides"]
# couriers = ["John", "Jim", "Jay", "Jack", "Jen"]
#order