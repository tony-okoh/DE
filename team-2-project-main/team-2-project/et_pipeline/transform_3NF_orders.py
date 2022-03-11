import pandas as pd
import datetime
import hashlib

def orders_normalised(df: pd.DataFrame, df_store: pd.DataFrame, df_customer: pd.DataFrame, df_payment_type:pd.DataFrame) -> pd.DataFrame:
    df_orders = df.drop(columns=['basket_items'])
    # Change data type of 'timestamp' from str to datetime
    df_orders['timestamp'] = df_orders['timestamp'].apply(lambda x: datetime.datetime.strptime(x,'%d/%m/%Y %H:%M'))
    # Create orders dataframe by merging with other dataframe to setup constraint with foreign key and by droping unnecessary columns.
    df_orders = pd.merge(df_orders,df_store, on='store_name', how='left')
    df_orders = pd.merge(df_orders,df_customer, on='customer_name', how='left')
    df_orders = pd.merge(df_orders,df_payment_type, on='payment_type_name', how='left')
    
    df_orders = df_orders.drop(columns=['store_name','customer_name','payment_type_name'])
    
    # Hashing columns and applying to id
    df_orders['order_id'] = df_orders.astype(str).iloc[:,:].sum(axis=1) # Adding each column as a str into a new column to be used as the base for the ID
    df_orders['order_id'] = df_orders['order_id'].apply(lambda x: str(hashlib.md5((x.strip()).encode('utf-8')).hexdigest()))
    
    df_orders = df_orders[['order_id','timestamp','store_id','customer_id','total_price','payment_type_id']]
    
    return df_orders

# Example
# from extract import extract_file
# from transform_sensitive_data import remove_sensitive_data
# from transform_3NF_store import store_normalised
# from transform_3NF_payment_type import payment_type_normalised
# from transform_3NF_customer import customer_normalised
# df = extract_file('chesterfield.csv')
# df = remove_sensitive_data(df,['card_number'])
# df_store = store_normalised(df)
# df_customer = customer_normalised(df)
# df_payment_type = payment_type_normalised(df)

# df = orders_normalised(df, df_store, df_customer, df_payment_type)

# print(df.head())
