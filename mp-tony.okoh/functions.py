import csv
import pandas
import pymysql
import os
from dotenv import load_dotenv
from prettytable import PrettyTable
from prettytable.prettytable import PrettyTable
from prettytable import from_db_cursor

def print_menu(item):
    print(item)
    
main_menu = "MAIN MENU\n----------\nActions\nEnter '1' for Product Menu\nEnter '2' for Courier Menu " \
                "\nEnter '3' for Order Menu\nEnter '0' to Exit\n"
                
product_menu = "\nPRODUCTS MENU\nEnter '0' to go back to MAIN MENU\nEnter '1' for PRODUCT LIST " \
                    "\nEnter '2' for NEW PRODUCT\nEnter '3' to UPDATE PRODUCT\nEnter '4' to DELETE PRODUCT " \
                    "\nEnter '5' to IMPORT DATA FROM CSV FILE: \n"

courier_menu = "\nCOURIER MENU\nEnter '0' to go back to MAIN MENU\nEnter '1' for COURIER LIST " \
                    "\nEnter '2' for NEW COURIER\nEnter '3' to UPDATE COURIER\nEnter '4' to DELETE COURIER " \
                    "\nEnter '5' to IMPORT DATA FROM CSV FILE: \n"
                    
order_menu = "\nORDER MENU\nEnter '0' to go back to MAIN MENU\nEnter '1' for ORDER LIST " \
                    "\nEnter '2' for NEW ORDER\nEnter '3' to UPDATE EXISTING ORDER STATUS " \
                    "\nEnter '4' to UPDATE EXISTING ORDER\nEnter '5' to DELETE ORDER " \
                    "\nEnter '6' to LIST ORDER BY STATUS/COURIER\nEnter '7' to IMPORT DATA FROM CSV FILE: \n"
                    
orders_status = ["PREPARING", "OUT FOR DELIVERY", "DELIVERED", "CANCELLED"]

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
    host,
    user,
    password,
    database
)
cursor = connection.cursor()

#------------------------------------------------PRODUCTS-------------------------------------------------#
# print product list
def print_prod_list():
    cursor.execute(f'SELECT * FROM products')
    products = from_db_cursor(cursor)
    print(products)
        
# add new product
def add_new_prod():
    while True:            
        try:
            print_prod_list()
            #user input
            Product_Name = input("\nEnter New Product Name: \n").title()
            Price = (input("Enter Price: \n")) 
            #check for null input
            if Product_Name and Price:           
                cursor.execute("""
                                INSERT INTO products (Product_Name, Price) 
                                VALUES (%s, %s)
                                """, (Product_Name, Price))
            #inserts only product name if price is empty 
            elif Product_Name and not Price: 
                cursor.execute("""
                                INSERT INTO products (Product_Name) 
                                VALUES (%s)
                                """, (Product_Name))
            #inserts only price if product name is empty
            elif not Product_Name and Price: 
                cursor.execute("""
                                INSERT INTO products (Price) 
                                VALUES (%s)
                                """, (Price))
            connection.commit()
            print('\nNew product added succesfully\n')
            #view added product
            view_result = "SELECT * FROM products ORDER BY product_id DESC LIMIT 1"
            cursor.execute(view_result)
            result = cursor.fetchone()
            print(result)
            break            
        except Exception as e:
            print(e)         
            print('Error: Note - Price must be Number')
            break
    
def update_prod():
    while True:
        try:
            print_prod_list()
            #user input
            product_ID = int(input("\nSelect Product ID to update: \n"))
            updated_product = input("\nEnter New Product Name: \n").title()
            updated_price = (input("Enter Price: \n"))
            #check for null input
            if product_ID and updated_product and updated_price:
                updates = "UPDATE products SET Product_Name = %s, Price = %s WHERE product_id = %s"
                val = (updated_product, updated_price, product_ID)         
                cursor.execute(updates, val) 
            #inserts only product name if price is empty 
            elif product_ID and updated_product and not updated_price:
                updates = "UPDATE products SET Product_Name = %s WHERE product_id = %s"
                val = (updated_product, product_ID)         
                cursor.execute(updates, val)  
            #inserts only price if product name is empty
            elif product_ID and not updated_product and updated_price:
                updates = "UPDATE products SET Price = %s WHERE product_id = %s"
                val = (updated_price, product_ID)         
                cursor.execute(updates, val)      
            connection.commit()
            print(cursor.rowcount, "record(s) updated")
            break
        except Exception as e:
            print(e)
            print('***Error: Note - Product ID/Price must be numbers***')
            break
            
# delete product
def delete_prod():
    while True:
        try:
            print_prod_list()
            #user input
            product_ID = int(input("\nSelect Product ID to delete: \n"))
            del_prod = "DELETE FROM products WHERE product_id = %s"
            val = (product_ID)
            cursor.execute(del_prod, val)
            connection.commit()
            print(cursor.rowcount, "record(s) deleted")
            break
        except:
            print('Error: Note - Product ID must be number')
            break            
    
#--------------------------------------------------COURIERS------------------------------------------------#   
# print courier list
def print_courier_list():
    cursor.execute(f'SELECT * FROM couriers')
    couriers = from_db_cursor(cursor)
    print(couriers)
        
# add new courier
def add_new_courier():
    while True:                    
        try:
            print_courier_list()
            #user input
            Cour_Name = input("\nEnter New Courier Name: \n").title()
            Cour_Phone = (input("Enter Courier Phone Number: \n")) 
            #check for null input
            if Cour_Name and Cour_Phone:           
                cursor.execute("""
                                INSERT INTO couriers (Courier_Name, Phone_Number) 
                                VALUES (%s, %s)
                                """, (Cour_Name, Cour_Phone))
            #inserts only courier name if courier phone is empty
            elif Cour_Name and not Cour_Phone:           
                cursor.execute("""
                                INSERT INTO couriers (Courier_Name) 
                                VALUES (%s)
                                """, (Cour_Name))
            #inserts only courier phone if courier name is empty
            elif not Cour_Name and Cour_Phone:           
                cursor.execute("""
                                INSERT INTO couriers (Phone_Number) 
                                VALUES (%s)
                                """, (Cour_Phone))
            connection.commit()
            print('\nNew courier added succesfully\n')
            #view added courier
            view_result = "SELECT * FROM couriers ORDER BY courier_id DESC LIMIT 1"
            cursor.execute(view_result)
            result = cursor.fetchone()
            print(result)
            break            
        except Exception as e:
            print(e)         
            print('Error: Please re-enter correct values')
            break
            
# update existing courier    
def update_courier():
    while True:
        try:
            print_courier_list()
            #user input
            cour_ID = int(input("\nSelect Courier ID to update: \n"))
            updated_cour = input("\nEnter New Courier Name: \n").title()
            updated_phone = (input("Enter Phone Number: \n")) 
            #check for null inputs           
            if cour_ID and updated_cour and updated_phone:
                updates = "UPDATE couriers SET Courier_Name = %s, Phone_Number = %s WHERE courier_id = %s"
                val = (updated_cour, updated_phone, cour_ID)         
                cursor.execute(updates, val)  
            #inserts only courier phone if courier name is empty
            elif cour_ID and not updated_cour and updated_phone:
                updates = "UPDATE couriers SET Phone_Number = %s WHERE courier_id = %s"
                val = (updated_phone, cour_ID)         
                cursor.execute(updates, val)
            #inserts only courier name if courier phone is empty
            elif cour_ID and updated_cour and not updated_phone:
                updates = "UPDATE couriers SET Courier_Name = %s WHERE courier_id = %s"
                val = (updated_cour, cour_ID)         
                cursor.execute(updates, val) 
            connection.commit()
            print(cursor.rowcount, "record(s) updated")
            break            
        except:           
            print('Error: Note - Courier ID/Phone Number must be numbers')
            break
    
# delete courier
def delete_courier():
    while True:
        try:
            print_courier_list()
            #user input
            courier_ID = int(input("\nSelect Courier ID to delete: \n"))
            del_cour = "DELETE FROM couriers WHERE courier_id = %s"
            val = (courier_ID)
            cursor.execute(del_cour, val)
            connection.commit()
            print(cursor.rowcount, "record(s) deleted") 
            break            
        except:           
            print('Error: Courier ID must be number')
            break   

#----------------------------------------------------ORDERS---------------------------------------------------#   
#print orders 
def print_order_list(): 
    cursor.execute(f'SELECT * FROM orders')
    orders = from_db_cursor(cursor)
    print(orders)   

#create orders   
def create_new_order():
    while True:
        try:
            #user input
            Customer_Name = input("Enter Name: \n").title()
            Customer_Address = input("Enter Address: \n").title()
            Customer_Phone = input("Enter Phone Number: \n")
            print_prod_list()
            #CONVERT prod_ID entries to list of integers
            item_list = []    
            while True:
                #user input
                item = str(input("\nSelect Product ID to add products: \n"))
                print('Press ENTER twice to proceed after selecting products')
                #stops if the input is any of these strings
                if item in ("","q","quit","e","end","exit"):
                    break
                #if the input is a number, add it to the items list.
                elif item.isdigit():
                    item_list.append(int(item))
                else:
                    #if input type is a string, try again 
                    print("Error: Invalid input, please try again or press enter to end list")
                print(item_list)
            #Convert the list to string to insert into the order table
            items = ','.join(str(i_list) for i_list in item_list)
            print('COURIERS LIST')
            print_courier_list()
            #user input
            courier_ID = int(input("\nEnter Courier ID to select Courier: \n"))
            status = orders_status[0]
            cursor.execute("""
                            INSERT INTO orders (Customer_name, Customer_address, Customer_phone, Courier, Statuss, Items) 
                            VALUES (%s, %s, %s, %s, %s, %s)
                            """, (Customer_Name, Customer_Address, Customer_Phone, courier_ID, status, items))
            connection.commit()
            print('\nNew order added succesfully\n') 
            #view added order       
            view_result = "SELECT * FROM orders ORDER BY order_id DESC LIMIT 1"
            cursor.execute(view_result)
            result = cursor.fetchone()
            print(result)
            break
        except Exception as e:
            print(e)
            print('Error: Error: Enter correct')
            break

#UPDATE existing order status
def update_ex_order_status():
    while True:
        try:
            print_order_list()
            #user input
            order_ID = int(input("\nSelect Order ID to update status: \n"))
            print('ORDER STATUS')
            for i, row in enumerate(orders_status):
                print(i,':',row)
            new_status = (input("\nPlease select status ID to update order: \n"))
            status = orders_status[new_status]
            update_status = "UPDATE orders SET Statuss = %s WHERE order_id = %s"
            val = (status, order_ID)      
            cursor.execute(update_status, val) 
            connection.commit()
            print(cursor.rowcount, "record(s) updated")
            break            
        except Exception as e:    
            print(e)       
            print('Error: Note - Order ID/Status ID must be numbers')
            break
    
#UPDATE existing order
def update_ex_order():
    while True:
        try:
            print_order_list()
            #user input
            order_ID = int(input("\nSelect Order ID to update: \n"))
            update_dict = {}            
            update_dict["Customer_name"] = input("\nEnter an updated Customer Name: \n").title()
            update_dict["Customer_address"] = input("\nEnter an updated Customer Address: \n").title()
            update_dict["Customer_phone"] = input("\nEnter an updated Customer Phone Number: \n")
            print_courier_list()
            update_dict["Courier"] = input("\nSelect an updated Courier ID to select Courier: \n")
            print('ORDER STATUS')
            for i, row in enumerate(orders_status):
                print(i,':',row)
            try:
                new_status = (input("\nSelect an updated Status ID to update status: \n"))
                update_dict["Statuss"] = orders_status[int(new_status)] 
            except:
                print('Status not updated\n')
            print_prod_list()
            #CONVERT above user input to list of integers
            item_list = []    
            while True:
                #asks for an input
                item = str(input("\nSelect Product ID to add products: \n"))
                #stops if the input is any of these strings
                if item in ("","q","quit","e","end","exit"):
                    break
                #if the input is a number, add it to the items list.
                elif item.isdigit():
                    item_list.append(int(item))
                else:
                    #if input type is a string, try again 
                    print("Error: Invalid input, please try again or press enter to end list")
                print(item_list)
            #Convert the list to string to insert into the order table
            items = ','.join(str(i_list) for i_list in item_list)   
            update_dict["Items"] = items            
            updates = []
            for key in update_dict:
                if update_dict[key]:
                    updates.append(f"{key}='{update_dict[key]}'")    
            update_order = f"UPDATE orders SET {','.join(updates)} WHERE order_id = %s"
            val = (order_ID)      
            cursor.execute(update_order, val) 
            connection.commit()
            print(cursor.rowcount, "record(s) updated")
            break
        except Exception as e:    
            print(e)       
            print('Error: Please re-enter correct values')  
            break
            
#Delete order
def delete_order():
    while True:
        try:
            print_order_list()
            #user input
            order_ID = int(input("\nSelect Order ID to delete: \n"))
            del_order = "DELETE FROM orders WHERE order_id = %s"
            val = (order_ID)
            cursor.execute(del_order, val)
            connection.commit()
            print(cursor.rowcount, "record(s) deleted")
            break
        except:
            print('Error: Note - Order ID must be number')
            break   
        
#List orders by status
def list_orders_by_status_or_courier():
    while True:
        try:
            sel = int(input("\nEnter '1' to list by STATUS\nEnter '2' to list by COURIER: \n"))
            if sel == 1:
                print('ORDER STATUS')
                for i, row in enumerate(orders_status):
                    print(i,':',row)
                #user input
                status_ind = int(input('\nPlease enter Status ID to select: \n'))
                status = orders_status[status_ind]
                order_list = "SELECT * FROM orders WHERE Statuss = %s"
                val = (status)
                cursor.execute(order_list, val)
                result = from_db_cursor(cursor)
                print(result)
                break
            elif sel == 2:
                print_courier_list()
                #user input
                courier_ID = (input("\nEnter Courier ID to select: \n"))
                order_list = "SELECT * FROM orders WHERE Courier = %s"
                val = (courier_ID)
                cursor.execute(order_list, val)
                result = from_db_cursor(cursor)
                print(result)
                break                
        except:
            print('Error: Note - Status ID is a number')    
            break                    

#export products to csv
def export_products_to_csv(): 
    # export from database to csv file using pandas 
    query = 'select * from miniproject.products'
    results = pandas.read_sql_query(query, connection)
    results.to_csv("products.csv", index=False)

# #export couriers to csv
def export_couriers_to_csv(): 
    # export from database to csv file using pandas 
    query = 'select * from miniproject.couriers'
    results = pandas.read_sql_query(query, connection)
    results.to_csv("couriers.csv", index=False)

# #export orders to csv
def export_orders_to_csv(): 
    # export from database to csv file using pandas 
    query = 'select * from miniproject.orders'
    results = pandas.read_sql_query(query, connection)
    results.to_csv("orders.csv", index=False)

#import data from csv
def import_file_from_csv(filename):
    with open(filename) as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            print(i,':',row)

#exit application and close connection
def exit_app():
    print("Exiting Application - Goodbye!")
    connection.commit()
    cursor.close()
    connection.close()
    return
