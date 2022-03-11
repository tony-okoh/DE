from extract import extract_file
from transform_sensitive_data import remove_sensitive_data
from transform_3NF_customer import customer_normalised
from transform_3NF_order_item import order_item_normalized
from transform_3NF_orders import orders_normalised
from transform_3NF_payment_type import payment_type_normalised
from transform_3NF_product import product_normalised
from transform_3NF_product_flavour import product_flavour_normalised
from transform_3NF_product_size import product_size_normalised
from transform_3NF_store import store_normalised
from loading import load_to_redshift
import pandas as pd
import logging

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)
def etl_pipeline(file_name:str) -> bool:
    # Extract
    df = extract_file(file_name)
    # Log success of the extract process.
    if type(df) != pd.DataFrame:
        LOGGER.warning(f'Extract part of ETL unsuccessful. File might be not in the right format')
        return False
    else: LOGGER.info('Extract part of the ETL successful.')
    
    # Transform, cleaning data
    df = remove_sensitive_data(df,['card_number'])
    # Log success of the remove sensitive data process.
    if type(df) != pd.DataFrame:
        LOGGER.warning(f'Removing sensitive part of ETL unsuccessful.')
        return False
    else: LOGGER.info('Removing sensitive part of the ETL successful.')
    
    # Transform to 3NF
    df_customer = customer_normalised(df)
    df_payment_type = payment_type_normalised(df)
    df_store = store_normalised(df)
    df_product_size = product_size_normalised(df)
    df_product_flavour = product_flavour_normalised(df)
    
    df_orders = orders_normalised(df,df_store,df_customer,df_payment_type)
    df_product = product_normalised(df,df_product_size,df_product_flavour)
    
    df_order_item = order_item_normalized(df,df_store,df_customer,df_payment_type,df_orders,df_product_size,df_product_flavour,df_product)
    # Log success of the remove sensitive data process.
    LOGGER.info('Transform part of the ETL successful.')
    
    # Loading and log success of the loading process with the number of records being loaded.
    num_of_new_record = load_to_redshift('customer',df_customer)
    LOGGER.info(f'Loaded customer data. Number of record added: {num_of_new_record}')
    num_of_new_record = load_to_redshift('payment_type',df_payment_type)
    LOGGER.info(f'Loaded payment_type data. Number of record added: {num_of_new_record}')
    num_of_new_record = load_to_redshift('store',df_store)
    LOGGER.info(f'Loaded store data. Number of record added: {num_of_new_record}')
    num_of_new_record = load_to_redshift('product_size',df_product_size)
    LOGGER.info(f'Loaded product_size data. Number of record added: {num_of_new_record}')
    num_of_new_record = load_to_redshift('product_flavour',df_product_flavour)
    LOGGER.info(f'Loaded product_flavour data. Number of record added: {num_of_new_record}')
    
    num_of_new_record = load_to_redshift('product',df_product)
    LOGGER.info(f'Loaded product data. Number of record added: {num_of_new_record}')
    num_of_new_record = load_to_redshift('orders',df_orders)
    LOGGER.info(f'Loaded orders data. Number of record added: {num_of_new_record}')
    
    num_of_new_record = load_to_redshift('order_item',df_order_item)
    LOGGER.info(f'Loaded order_item data. Number of record added: {num_of_new_record}')
    
    return True # Return the success of the ETL process 