import pandas as pd
import hashlib

def get_flavour(basket_item:str) -> str:
    full_product_name_list = basket_item.split('-')
    if len(full_product_name_list) == 3: return full_product_name_list[1].strip()
    else: return 'NaN'

def product_flavour_normalised(df: pd.DataFrame)-> pd.DataFrame:
    s_product_flavour: pd.Series = df['basket_items']
    s_product_flavour = s_product_flavour.apply(lambda x: x.split(','))
    s_product_flavour = s_product_flavour.explode()
    s_product_flavour = s_product_flavour.apply(get_flavour)
    
    s_product_flavour = s_product_flavour.drop_duplicates()
    s_product_flavour = s_product_flavour.reset_index(drop=True)
    
    # Transforming series to DataFrame
    df_product_flavour: pd.DataFrame = s_product_flavour.to_frame().reset_index()
    # Changing column name
    df_product_flavour = df_product_flavour.rename(columns= {'index':'product_flavour_id','basket_items':'product_flavour_name'}) 
    # # Hash to produce ID
    df_product_flavour['product_flavour_id'] = df_product_flavour['product_flavour_name'].apply(lambda x: hashlib.md5((x.strip()).encode('utf-8')).hexdigest())
    
    df_product_flavour = df_product_flavour[['product_flavour_id','product_flavour_name']]
    
    return df_product_flavour





# Example
# from extract import extract_file
# from transform_sensitive_data import remove_sensitive_data
# df = extract_file('chesterfield.csv')
# df = remove_sensitive_data(df,['card_number'])
# df = product_flavour_normalised(df)

# print(df)
