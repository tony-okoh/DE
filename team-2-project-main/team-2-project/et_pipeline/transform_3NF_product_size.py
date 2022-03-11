import pandas as pd
import hashlib

def get_product_size(basket_item:str) -> str:
    return basket_item.strip().split(' ')[0]

def product_size_normalised(df: pd.DataFrame) -> pd.DataFrame:
    s_product_size: pd.Series = df['basket_items']
    s_product_size = s_product_size.apply(lambda x: x.strip().split(','))
    s_product_size = s_product_size.explode()
    
    s_product_size = s_product_size.apply(get_product_size)
    s_product_size = s_product_size.drop_duplicates()
    s_product_size = s_product_size.reset_index(drop=True)
    
    # Transforming series to DataFrame
    df_product_size: pd.DataFrame = s_product_size.to_frame().reset_index()
    # Changing column name
    df_product_size = df_product_size.rename(columns= {'index':'product_size_id','basket_items':'product_size_name'}) 
    # # Hash to produce ID
    df_product_size['product_size_id'] = df_product_size['product_size_name'].apply(lambda x: hashlib.md5((x.strip()).encode('utf-8')).hexdigest())
    
    df_product_size = df_product_size[['product_size_id','product_size_name']]
    
    return df_product_size



# Example 
# from extract import extract_file

# from transform_sensitive_data import remove_sensitive_data
# df = extract_file('chesterfield.csv')
# df = remove_sensitive_data(df,['card_number'])
# df = product_size_normalised(df)

# print(df)
