from typing import Dict, List, Union
from et_pipeline.extract import extract_file
from et_pipeline.transform_sensitive_data import remove_sensitive_data
from et_pipeline.transform_3NF_customer import customer_normalised
from et_pipeline.transform_3NF_order_item import order_item_normalized
from et_pipeline.transform_3NF_orders import orders_normalised
from et_pipeline.transform_3NF_payment_type import payment_type_normalised
from et_pipeline.transform_3NF_product import product_normalised
from et_pipeline.transform_3NF_product_flavour import product_flavour_normalised
from et_pipeline.transform_3NF_product_size import product_size_normalised
from et_pipeline.transform_3NF_store import store_normalised
import pandas as pd
import logging
import boto3
from io import StringIO
import datetime
import os

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
load_bucket_name = os.getenv('LOAD_BUCKET_NAME') # Retrieve environment variable
def et_pipeline(file_name:str, key_name:str) -> bool:
    # Extract
    df = extract_file(file_name)
    # Log success of the extract process.
    if type(df) != pd.DataFrame:
        LOGGER.warning(f'Extract part of ET unsuccessful. File might be not in the right format')
        return False
    else: LOGGER.info('Extract part of the ET successful.')
    
    # Transform, cleaning data
    df = remove_sensitive_data(df,['card_number'])
    # Log success of the remove sensitive data process.
    if type(df) != pd.DataFrame:
        LOGGER.warning(f'Removing sensitive part of ET unsuccessful.')
        return False
    else: LOGGER.info('Removing sensitive part of the ET successful.')
    
    # Transform to 3NF
    df_customer = customer_normalised(df)
    df_payment_type = payment_type_normalised(df)
    df_store = store_normalised(df)
    df_product_size = product_size_normalised(df)
    df_product_flavour = product_flavour_normalised(df)
    
    df_orders = orders_normalised(df,df_store,df_customer,df_payment_type)
    df_product = product_normalised(df,df_product_size,df_product_flavour)
    
    df_order_item = order_item_normalized(df,df_store,df_customer,df_payment_type,df_orders,df_product_size,df_product_flavour,df_product)
    # Log success of transform to 3NF
    LOGGER.info('Transform part of the ET successful.')
    
    # Upload DataFrames as csv to s3 load bucket
    df_dict_list: List[Dict[str,Union[str,pd.DataFrame]]] = [{"table":"customer","df":df_customer},
                                {"table":"payment_type","df":df_payment_type},
                                {"table":"store","df":df_store},
                                {"table":"product_size","df":df_product_size},
                                {"table":"product_flavour","df":df_product_flavour},
                                {"table":"product","df":df_product},
                                {"table":"orders","df":df_orders},
                                {"table":"order_item","df":df_order_item}]
    upload_dataframe(df_dict_list=df_dict_list,key_name=key_name)
    
    return True # Return the success of the ET process

def upload_dataframe(df_dict_list: List[Dict[str,Union[str,pd.DataFrame]]],key_name:str):
    for df_dict in df_dict_list:
        csv_buffer = StringIO()
        df_dict["df"].to_csv(csv_buffer, index=False)
        key_name = key_name.replace('/', '-')
        file_name = f"{df_dict['table']}-from-{key_name}-processed-at-{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.csv"
        s3_resource.Object(load_bucket_name, file_name).put(Body=csv_buffer.getvalue())
