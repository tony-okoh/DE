from functions import *

# PRINT main menu options

while True:
    print_menu(main_menu)
    Selection1 = int(input("Enter Selection: "))
    if Selection1 == 0:
        #persist data to csv file
        export_products_to_csv()
        export_couriers_to_csv()
        export_orders_to_csv()
        #exit application
        exit_app()
        break
    
#---------------------------------------------------PRODUCT MENU-------------------------------------------------#
#PRODUCT MENU
    if Selection1 == 1:      
        while True:
            try:
                print_menu(product_menu)         
                Selection2 = (int(input("Enter Menu Selection(Number): ")))
                if Selection2 == 0:
                    break
#PRINT PRODUCTS            
                while True:
                    if Selection2 == 1:                    
                        print_prod_list()
                        break 
#ADD NEW PRODUCT
                    elif Selection2 == 2:                    
                        add_new_prod()            
                        break
#UPDATE PRODUCT
                    elif Selection2 == 3:                    
                        update_prod()            
                        break
#DELETE PRODUCT
                    elif Selection2 == 4:                    
                        delete_prod()
                        break
#IMPORT DATA FROM CSV
                    elif Selection2 == 5:                    
                        import_file_from_csv('products.csv')
                        break
#RETURN TO MENU                    
                    else:
                        break
            except Exception as e:
                print(e)
                print('Please enter Number to proceed')
                break

#----------------------------------------------------COURIER MENU-------------------------------------------------#
#COURIER MENU
    if Selection1 == 2:      
        while True:
            try:
                print_menu(courier_menu)         
                Selection2 = (int(input("Enter Menu Selection(Number): ")))
                if Selection2 == 0:
                    break
#PRINT COURIERS            
                while True:
                    if Selection2 == 1:
                        print_courier_list()
                        break 
#ADD NEW COURIER
                    elif Selection2 == 2:                        
                        add_new_courier()            
                        break
#UPDATE COURIER
                    elif Selection2 == 3:                        
                        update_courier()            
                        break
#DELETE COURIER
                    elif Selection2 == 4:                        
                        delete_courier()
                        break
#IMPORT DATA FROM CSV
                    elif Selection2 == 5:                    
                        import_file_from_csv('couriers.csv')
                        break
#RETURN TO MENU                    
                    else:
                        break                    
            except Exception as e:
                print(e)
                print('Please enter Number to proceed')
                break    
#-----------------------------------------------------ORDER MENU---------------------------------------------------#
#ORDER MENU
    if Selection1 == 3:
        while True:
            try:
                print_menu(order_menu)         
                Selection2 = (int(input("Enter Menu Selection(Number): ")))
                if Selection2 == 0:
                    break
#PRINT ORDERS            
                while True:
                    if Selection2 == 1:
                        print_order_list()
                        break 
#CREATE NEW ORDER
                    elif Selection2 == 2:                        
                        create_new_order()
                        break
#UPDATE EXISTING ORDER STATUS
                    elif Selection2 == 3:                        
                        update_ex_order_status()
                        break                                  
#UPDATE EXISTING ORDER                     
                    elif Selection2 == 4:                        
                        update_ex_order()
                        break
#DELETE ORDER                     
                    elif Selection2 == 5:                        
                        delete_order()
                        break
#DELETE ORDER                     
                    elif Selection2 == 6:                        
                        list_orders_by_status_or_courier()
                        break 
#IMPORT DATA FROM CSV
                    elif Selection2 == 7:                    
                        import_file_from_csv('orders.csv')
                        break
#RETURN TO MENU                    
                    else:
                        break            
            except Exception as e:
                print(e)
                print('Please enter Number to proceed')
                break
            
#end
