import pandas as pd
import hashlib

def customer_normalised(df:pd.DataFrame) -> pd.DataFrame:
    s_customer: pd.Series = df['customer_name']
    s_customer = s_customer.drop_duplicates()
    s_customer = s_customer. reset_index(drop=True)
    # changing series to dataframe 
    # to.frame to reset create a DataFrame with a column containing the Index.
    df_customer: pd.DataFrame = s_customer.to_frame().reset_index()
    # This wiil change the  column name
    df_customer = df_customer.rename(columns= {'index':'customer_id'})
    # this will Hash to customer name
    #apply() method allows you to apply a function which return the index
    df_customer['customer_id'] = df_customer['customer_name'].apply(lambda x: hashlib.md5((x.strip()).encode('utf-8')).hexdigest())
    df_customer = df_customer[['customer_id','customer_name']]
    
    return df_customer

# Example
# from extract import extract_file
# from transform_sensitive_data import remove_sensitive_data
# df = extract_file('chesterfield.csv')
# df = remove_sensitive_data(df,['card_number'])
# df = customer_normalised(df)
# print(df.tail(10))
