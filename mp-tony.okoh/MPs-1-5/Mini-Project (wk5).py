import csv
import pandas as pd
import pyodbc
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
        
       

#export products to csv
def export_products_to_csv(): 
    # export from database to csv file using pandas and pydbc
    sql_query = pd.read_sql_query('''
                                select * from miniproject.products
                                '''
                                ,connection)
    df = pd.DataFrame(sql_query)
    df.to_csv (r'C:\Users\User\Desktop\Mini-Project\products.csv', index = False)

#export couriers to csv
def export_couriers_to_csv(): 
    sql_query = pd.read_sql_query('''
                                select * from miniproject.couriers
                                '''
                                ,connection)
    df = pd.DataFrame(sql_query)
    df.to_csv (r'C:\Users\User\Desktop\Mini-Project\couriers.csv', index = False)

#export orders to csv
def export_orders_to_csv(): 
    sql_query = pd.read_sql_query('''
                                select * from miniproject.orders
                                '''
                                ,connection)
    df = pd.DataFrame(sql_query)
    df.to_csv (r'C:\Users\User\Desktop\Mini-Project\orders.csv', index = False)

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