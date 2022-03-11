
from my_functions import *

import csv

products = open_file('products.csv')
couriers = open_file('couriers.csv')
orders = open_file('orders.csv')

orders_status = ["PREPARING", "OUT FOR DELIVERY", "DELIVERED"]

#******************MAIN FUNCTIONS******************#

while True:
    print_menu(main_menu)
    Selection1 = int(input("Enter Selection: "))
    if Selection1 == 0:
        write_to_products('products.csv', products)
        write_to_courier("couriers.csv", couriers)
        # write_to_orders("orders.csv", orders)
        print("Exiting Application - Goodbye!")
        break

#---------------PRODUCT MENU--------------#

#print products menu
    if Selection1 == 1:      
        while True:
            print_menu(product_menu)         
            Selection2 = (int(input("Enter Menu Selection(Number): ")))
            if Selection2 == 0:
                break
#print products list
            while True:
                if Selection2 == 1:
                    read_file('products.csv')
                    break                     
#create new product                
                elif Selection2 == 2:                                        
                    class products_list:
                        def __init__(self, PRODUCT_NAME, PRICE):
                            self.PRODUCT_NAME = PRODUCT_NAME
                            self.PRICE = PRICE                        
                        def new_PRODUCT_NAME(self, PRODUCT_NAME):
                            self.PRODUCT_NAME = PRODUCT_NAME
                        def new_PRICE(self, PRICE):
                            self.PRICE = PRICE                           
                                            
                    Products_list = products_list('None', 00000)                    
                    PRODUCT_NAME = input("\nEnter New Product Name: \n").title()
                    PRICE = float(input("Enter Price: \n"))               
                    Products_list.new_PRODUCT_NAME(PRODUCT_NAME)
                    Products_list.new_PRICE(PRICE)                    
                    print(f"{Products_list.PRODUCT_NAME}: {Products_list.PRICE}") 
                    print('\n')                    
                    with open('products.csv','a',newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow([Products_list.PRODUCT_NAME, Products_list.PRICE])
                    f.close()
                    read_file('products.csv')
                    products = open_file('products.csv')
                    break
#update existing product                
                elif Selection2 == 3:
                    with open("products.csv") as f:
                        reader = csv.DictReader(f)
                        reader = [x for x in reader]
                        print('EXISTING PRODUCT LIST')
                        for i, row in enumerate(reader):
                            print(i,':',row)
                    
                        product_index = int(input("\nEnter Product ID Number: "))
                        new_product = (input("Enter New Product Name: ")).title()
                        new_price = float(input("\nEnter Product Price: "))
                        print("\n")
                        
                        update_products = reader[product_index]
                        update_products.update(PRODUCT_NAME = new_product)
                        update_products.update(PRICE = new_price)
                        print(update_products)
                        print('\n')
                        write_to_products('products.csv', reader)
                        read_file('products.csv')
                        products = open_file('products.csv')
                        break
#delete a product                
                elif Selection2 == 4:
                    with open("products.csv") as f:
                        reader = csv.DictReader(f)
                        reader = [x for x in reader]
                        print('EXISTING PRODUCT LIST')
                        for i, row in enumerate(reader):
                            print(i,':',row)
                        product_index = (int(input("\nEnter Product ID Number to Delete:\n")))
                        print(f"You are deleting: {product_index} =", reader.pop(product_index))
                        print("\n")
                        print("The New Product List:")
                        write_to_products('products.csv', reader)
                        read_file('products.csv')
                        products = open_file('products.csv')
                        break      

#---------------------COURIER MENU--------------------#

    if Selection1 == 2:      
        while True:
            print_menu(courier_menu)          
            Selection2 = (int(input("Enter Courier Menu Selection(Number): ")))
            if Selection2 == 0:
                break
#print courier list                  
            while True:
                if Selection2 == 1:
                    read_file('couriers.csv')
                    break                     
#create new courier                
                elif Selection2 == 2:                                        
                    class couriers_list:
                        def __init__(self, COURIER_NAME, PHONE_NUMBER):
                            self.COURIER_NAME = COURIER_NAME
                            self.PHONE_NUMBER = PHONE_NUMBER                       
                        def new_COURIER_NAME(self, COURIER_NAME):
                            self.COURIER_NAME = COURIER_NAME
                        def new_PHONE_NUMBER(self, PHONE_NUMBER):
                            self.PHONE_NUMBER = PHONE_NUMBER                           
                                            
                    Couriers_list = couriers_list('None', 00000)                    
                    COURIER_NAME = input("\nEnter New Courier Name: \n").title()
                    PHONE_NUMBER = int(input("Enter Phone Number: \n"))               
                    Couriers_list.new_COURIER_NAME(COURIER_NAME)
                    Couriers_list.new_PHONE_NUMBER(PHONE_NUMBER)                    
                    print(f"{Couriers_list.COURIER_NAME}: {Couriers_list.PHONE_NUMBER}") 
                    print('\n')
                    import csv
                    with open('couriers.csv','a',newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow([Products_list.COURIER_NAME, Products_list.PHONE_NUMBER])
                    f.close()
                    read_file('couriers.csv')
                    couriers = open_file('couriers.csv')
                    break
#update existing courier                
                elif Selection2 == 3:
                    with open("couriers.csv") as f:
                        reader = csv.DictReader(f)
                        reader = [x for x in reader]
                        print('EXISTING COURIER LIST')
                        for i, row in enumerate(reader):
                            print(i,':',row)
                    
                        courier_index = int(input("\nEnter Courier ID Number: "))
                        new_courier = (input("Enter New Courier Name: ")).title()
                        new_phone_num = int(input("\nEnter New Courier Phone Number: "))
                        print("\n")                        
                        update_couriers = reader[courier_index]
                        update_couriers.update(COURIER_NAME = new_courier)
                        update_couriers.update(PRICE = new_phone_num)
                        print(update_couriers)
                        print('\n')
                        write_to_courier('couriers.csv', reader)
                        read_file('couriers.csv')
                        couriers = open_file('couriers.csv')
                        break
#delete a courier                
                elif Selection2 == 4:
                    with open("couriers.csv") as f:
                        reader = csv.DictReader(f)
                        reader = [x for x in reader]
                        print('EXISTING COURIER LIST')
                        for i, row in enumerate(reader):
                            print(i,':',row)
                        courier_index = (int(input("\nEnter Courier ID Number to Delete:\n")))
                        print(f"You are deleting: {courier_index} =", reader.pop(courier_index))
                        print("\n")
                        print("The New Courier List:")
                        write_to_courier('couriers.csv', reader)
                        read_file('couriers.csv')
                        couriers = open_file('couriers.csv')
                        break
                    
#----------------ORDERS MENU------------------#

    if Selection1 == 3: 
        while True:
            print_menu(order_menu)           
            Selection2 = (int(input("Enter Order Menu Selection(Number): ")))
#return to main menu
            if Selection2 == 0:
                break
#print order list
            while True:
                if Selection2 == 1:
                    read_file('orders.csv')
                    print(orders)                   
                    break                                        
# # create order list from customer input                   
                if Selection2 == 2:
                    class orders_list:
                        def __init__(self, Customer_Name, Customer_Address, Customer_Phone, Courier, Status):
                            self.Customer_Name = Customer_Name
                            self.Customer_Address = Customer_Address
                            self.Customer_phone = Customer_Phone
                            self.Courier = Courier
                            self.Status = Status
                            
                        def update_Customer_Name(self, Customer_Name):
                            self.Customer_Name = Customer_Name
                        def update_Customer_Address(self, Customer_Address):
                            self.Customer_Address = Customer_Address   
                        def update_Customer_Phone(self, Customer_Phone):
                            self.Customer_Phone = Customer_Phone   
                        def update_Courier(self, Courier):
                            self.Courier = Courier  
                                            
                    Orders_list = orders_list('None', 'None', 00000, 'None', 'PREPARING')                    
                    Customer_Name = input("Enter Name: \n").title()
                    Customer_Address = input("Enter Address: \n").title()
                    Customer_Phone = int(input("Enter Phone Number: \n"))                    
                    print("\nCouriers")
                    for index, value in enumerate(couriers):
                        print(index, value)
                    courier_index_num = int(input("\nEnter courier index number to select courier: "))
                    print(couriers[courier_index_num], '\n')
                    Courier = couriers[courier_index_num]
                    Orders_list.update_Customer_Name(Customer_Name)
                    Orders_list.update_Customer_Address(Customer_Address)
                    Orders_list.update_Customer_Phone(Customer_Phone)
                    Orders_list.update_Courier(Courier)
                    print(f"{Orders_list.Customer_Name}\n{Orders_list.Customer_Address}") 
                    print(f"{Orders_list.Customer_Phone}\n{Orders_list.Courier}\n{Orders_list.Status}")
                    new_order = [Orders_list.Customer_Name, Orders_list.Customer_Address, 
                                            Orders_list.Customer_Phone,Orders_list.Courier, Orders_list.Status]                     
                    with open('orders.csv','a',newline='') as f:
                        writer=csv.writer(f)
                        writer.writerow(new_order)
                        orders = open_file('orders.csv')
                        break
                    
#update the existing order status          
                if Selection2 == 3:                    
                    with open("orders.csv") as f:
                        reader = csv.DictReader(f)
                        reader = [x for x in reader]
                        print('\n')
                        for i, row in enumerate(reader):
                            print(i,':',row)
                        order_to_update_status = int(input("\nSelect order number to update status: "))   
                        print('\n') 
                        updated_status = reader[order_to_update_status]
                                                
                        for i, v in enumerate(orders_status):   
                            print(i, v)                                
                        sel_status = int(input("\nSelect status ID to update status: "))
                        print('\n')
                        updated_status = {k.strip(): v for (k, v) in updated_status.items()}

                        updated_status.update(Status = orders_status[sel_status])
                        print(updated_status)
                        with open("orders.csv", 'w', newline="") as f:
                            fieldnames = ["Customer_Name", "Customer_Address", "Customer_Phone", "Courier", "Status"]
                            writer = csv.DictWriter(f, fieldnames=fieldnames)                            
                            writer.writeheader()
                            writer.writerows(updated_status) 

                        # orders = open_file('orders.csv')                            
                        break
                            
# STRETCH - UPDATE existing order
                if Selection2 == 4:                    
                    with open("orders.csv") as f:
                        reader = csv.DictReader(f)
                        reader = [x for x in reader]
                        print('EXISTING ORDER LIST')
                        for i, row in enumerate(reader):
                            print(i,':',row)
                        try:
                            ex_order_to_update = int(input("\nSelect order ID to update(Enter Number): ")) 
                        except Exception as e:
                            print('Please enter Order ID: ' + str(e))  
                            break                      
                        update_ex_order = reader[ex_order_to_update]
                        
                        c_name = input("Update Customer Name(Or Press 'Enter' to skip): ").title()
                        if len(c_name) == 0:
                            c_name = update_ex_order.get('Customer_Name')                            
                        else:
                            update_ex_order.update(Customer_Name = c_name)
                        
                        c_address = input("Update Customer Address(Or Press 'Enter' to skip): ").title()
                        if len(c_address) == 0:
                            c_address = update_ex_order.get('Customer_Address') 
                        else:
                            update_ex_order.update(Customer_Address = c_address)
                        
                        c_phone = input("Update Customer Phone(Or Press 'Enter' to skip): ")
                        if len(c_phone) == 0:
                            c_phone = update_ex_order.get('Customer_Phone') 
                        else:
                            update_ex_order.update(Customer_Phone = c_phone)
                        
                        print(f"\nCOURIERS\n")
                        for index, value in enumerate(couriers):
                            print(index, value)
                            
                        c_courier = input("Update Courier(Enter '0' to update Or Press 'Enter' to skip): ")
                        if len(c_courier) == 0:
                            c_courier = update_ex_order.get('Courier') 
                        else:                            
                            courier_index_num = int(input("\nEnter courier index number to select courier: "))
                            c_courier = couriers[courier_index_num]
                            update_ex_order.update(Courier = c_courier)
                        
                        print(f"\nORDERS STATUS\n")
                        for i, v in enumerate(orders_status):   
                                print(i, v)
                        c_status = input("Update Order Status(Enter '0' to update Or Press 'Enter' to skip): ")
                        if len(c_status) == 0:
                            c_status = update_ex_order.get('Status') 
                        else:
                            sel_status = int(input("\nSelect status to update: "))
                            c_status = orders_status[sel_status]
                            update_ex_order.update(Status = c_status)                                                
                        print(update_ex_order) 
                            
                        with open("orders.csv", 'w', newline="") as f:
                            fieldnames = ["Customer_Name", "Customer_Address", "Customer_Phone", "Courier", "Status"]
                            writer = csv.DictWriter(f, fieldnames=fieldnames)                            
                            writer.writeheader()
                            writer.writerows(reader)                                                                        
                            
                            break                        

#delete courier                 
                if Selection2 == 5:                    
                    with open("orders.csv") as f:
                        reader = csv.DictReader(f)
                        reader = [x for x in reader]
                        print('EXISTING ORDER LIST')
                        for i, row in enumerate(reader):
                            print(i,':',row)
                        ex_order_to_update = int(input("\nSelect order to update(Enter Number): ")) 
                        update_ex_order = reader[ex_order_to_update]                    
                        d_courier = int(input("Enter '3' to Delete Courier"))
                        if d_courier == 3:
                            d_courier = update_ex_order.pop('Courier')
                            print(update_ex_order)
                            break