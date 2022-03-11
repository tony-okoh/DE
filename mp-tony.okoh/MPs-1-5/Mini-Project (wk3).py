# Import product and courier lists from .txt files

def read_file(filename):
    file = open(filename, "r")
    product = file.read()
    products = product.split()
    file.close()
    return products

products = read_file("products.txt")
couriers = read_file('couriers.txt')

#dump product and courier lists into file.txt 
def write_file(filename, items):        
    file = open(filename, 'w')
    for item in items:
        file.write(item + '\n')
    file.close()
    
#orders list of dictionaries
orders = {
    "Customer_Name:": "No entry",
    "Customer_Address:": "No entry",
    "Customer_Phone:": "No entry",
    "Courier:": "No entry",
    "Status:": "None"
    }

orders_status = ["PREPARING", "OUT FOR DELIVERY", "DELIVERED"]

#******************MAIN FUNCTIONS******************
#print main menu
while True:
    print("MAIN MENU\n----------\nActions\nEnter '1' for Product Menu\nEnter '2' for Courier Menu\nEnter '3' for Order Menu\nEnter '0' to Exit\n")
    Selection1 = int(input("Enter Selection: "))
    if Selection1 == 0:
#dump products and courier lists into file.txt and exit app
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
#print products list
            while True:
                if Selection2 == 1:
                    print(f"\n{products}")
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
                    user_value = (input("Enter new product name: ")).lower()
                    print("\n")
                    products[user_index] = user_value
                    print("Updated Product List:")
                    for index, value in enumerate(products):                        
                        print(index, value)
                    break
#delete a product                
                elif Selection2 == 4:
                    for index, value in enumerate(products):
                        print(index, value)                    
                    product_index = (int(input("\nEnter product number to delete:\n")))
                    print(f"You are deleting: {product_index} =", products.pop(product_index))
                    print("\n")
                    print("The New Product List:")
                    for index, value in enumerate(products): 
                        print(index, value)                       
                    break
    if Selection1 == 2:      
        while True:
            print("\nCOURIER MENU\nEnter '0' to go back to MAIN MENU\nEnter '1' for COURIER LIST\n"
                    "Enter '2' for NEW COURIER\nEnter '3' to UPDATE COURIER\nEnter '4' to DELETE COURIER: \n")            
            Selection2 = (int(input("Enter Courier Menu Selection(Number): ")))
            if Selection2 == 0:
                break
#create courier list from customer input                   
            while True:
                if Selection2 == 1:
                    print(f"\n{couriers}")  
                    break                
#create a new courier                
                elif Selection2 == 2:
                    couriers.append(input("Add New courier: "))   
                    print("You have added a new courier\n")                 
                    print("New product list: ",couriers)
                    break  
#update existing courier list                
                elif Selection2 == 3:
                    for index, value in enumerate(couriers):
                        print(index, value)
                    user_index = int(input("\nEnter courier number: "))
                    user_value = (input("Enter new courier name: ")).lower()
                    print("\n")
                    couriers[user_index] = user_value
                    print("Updated Courier List:")
                    for index, value in enumerate(couriers):                        
                        print(index, value)
                    break
#delete courier                
                elif Selection2 == 4:
                    for index, value in enumerate(couriers):
                        print(index, value)                    
                    courier_index = (int(input("\nEnter courier number to delete:\n")))
                    print(f"You are deleting: {courier_index} =", couriers.pop(courier_index))
                    print("\n")
                    print("The New Courier List:")
                    for index, value in enumerate(couriers): 
                        print(index, value)                       
                    break
    if Selection1 == 3: 
        while True:
            print("\nORDER MENU\nEnter '0' to go back to MAIN MENU\nEnter '1' for ORDER LIST\n"
                    "Enter '2' for NEW ORDER\nEnter '3' to UPDATE EXISTING ORDER STATUS\n"
                    "Enter '4' to UPDATE EXISTING ORDER\nEnter '5' to DELETE ORDER: \n")            
            Selection2 = (int(input("Enter Order Menu Selection(Number): ")))
#return to main menu
            if Selection2 == 0:
                break
#print order list
            while True:
                if Selection2 == 1:
                    for k, v in orders.items():
                        print('\n',k, '-->', v)                    
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
                    Customer_Address = input("Enter Address: \n")
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
                    import csv
                    with open('orders.csv','a',newline='') as f:
                        writer=csv.writer(f)
                        writer.writerow([Orders_list.Customer_Name, Orders_list.Customer_Address, Orders_list.Customer_Phone,Orders_list.Courier, Orders_list.Status])
                        break
#update the existing order status          
                if Selection2 == 3:
                    from csv import reader                 
                    with open('orders.csv', 'r') as read_obj:
                        csv_reader = reader(read_obj)
                        header = next(csv_reader)    
                        if header != None:     
                            for row in csv_reader:
                                for index, value in enumerate(row):
                                    print(index, value)
                                order_status_index = int(input("\nEnter order status index number: "))
                                order_status_value = (input("Enter new order status: ")).upper()
                                print("\n")
                                row[order_status_index] = order_status_value
                                print("Updated order status:")
                                for index, value in enumerate(row):                        
                                    print(index, value)
                                break
