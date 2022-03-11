import pandas as pd
import hashlib
import datetime
from et_pipeline.transform_3NF_product import get_product_name, get_product_price
from et_pipeline.transform_3NF_product_flavour import get_flavour
from et_pipeline.transform_3NF_product_size import get_product_size

def order_item_normalized(df: pd.DataFrame, df_store:pd.Series, df_customer:pd.Series, df_payment_type:pd.Series, df_orders: pd.DataFrame, df_product_size: pd.Series, df_product_flavour: pd.Series, df_product: pd.DataFrame) -> pd.DataFrame:
    df_order_item: pd.DataFrame = df
    # Transform data to setup foreign key constraint for orders table
    df_order_item['basket_items'] = df_order_item['basket_items'].apply(lambda x: x.split(','))
    df_order_item = df_order_item.explode('basket_items')
    df_order_item['timestamp'] = df_order_item['timestamp'].apply(lambda x: datetime.datetime.strptime(x,'%d/%m/%Y %H:%M'))
    
    # Transform data to setup foreign key constraint for product table
    df_order_item['product_name'] = df_order_item['basket_items'].apply(get_product_name)
    df_order_item['product_size_name'] = df_order_item['basket_items'].apply(get_product_size)
    df_order_item['product_flavour_name'] = df_order_item['basket_items'].apply(get_flavour)
    df_order_item['product_price'] = df_order_item['basket_items'].apply(get_product_price)
    
    # Create order_item dataframe by merging with orders dataframe (and its foreign constraints) to setup constraint with foreign key
    df_order_item = pd.merge(df_order_item,df_product_size,on='product_size_name',how='left')
    df_order_item = pd.merge(df_order_item,df_product_flavour,on='product_flavour_name',how='left')
    
    df_order_item = pd.merge(df_order_item,df_product,on=['product_name','product_size_id','product_flavour_id','product_price'],how='left')
    
    # Create order_item dataframe by merging with product dataframe (and its foreign constraints) to setup constraint with foreign key
    df_order_item = pd.merge(df_order_item,df_store, on='store_name')
    df_order_item = pd.merge(df_order_item,df_customer, on='customer_name')
    df_order_item = pd.merge(df_order_item,df_payment_type, on='payment_type_name')
    
    df_order_item = pd.merge(df_order_item,df_orders, on=['timestamp','total_price','store_id','customer_id','payment_type_id'],how='left')
    
    # Drop all columns but order_id and product_id
    df_order_item = df_order_item[['order_id','product_id']]
    
    # Remove duplicate and create new columns of the quantities of each duplication removed
    df_order_item = df_order_item.groupby(df_order_item.columns.tolist(),as_index=False).size()
    df_order_item = df_order_item.rename(columns={'size':'quantity'})
    
    # Hashing columns and applying to id
    df_order_item['order_item_id'] = df_order_item.astype(str).iloc[:,:].sum(axis=1) # Adding each column as a str into a new column to be used as the base for the ID
    df_order_item['order_item_id'] = df_order_item['order_item_id'].apply(lambda x: str(hashlib.md5((x.strip()).encode('utf-8')).hexdigest()))
    
    df_order_item = df_order_item[['order_id','product_id','quantity','order_item_id']]
    
    return df_order_item




# Example
# from extract import extract_file
# from transform_3NF_store import store_normalised
# from transform_3NF_payment_type import payment_type_normalised
# from transform_3NF_customer import customer_normalised
# from transform_sensitive_data import remove_sensitive_data
# from transform_3NF_product_flavour import product_flavour_normalised
# from transform_3NF_product_size import product_size_normalised
# from transform_3NF_orders import orders_normalised
# from transform_3NF_product import product_normalised
# df = extract_file('chesterfield.csv')
# df = remove_sensitive_data(df,['card_number'])
# df_store_1 = store_normalised(df)
# df_customer_1 = customer_normalised(df)
# df_payment_type_1 = payment_type_normalised(df)
# df_orders_1 = orders_normalised(df, df_store_1, df_customer_1, df_payment_type_1)

# df_product_size_1 = product_size_normalised(df)
# df_product_flavour_1 = product_flavour_normalised(df)
# df_product_1 = product_normalised(df, df_product_size_1, df_product_flavour_1)

# df = order_item_normalized(df,df_store_1,df_customer_1,df_payment_type_1, \
#     df_orders_1,df_product_size_1,df_product_flavour_1,df_product_1)

# print(df)
