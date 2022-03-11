import pandas as pd
import hashlib
from et_pipeline.transform_3NF_product_flavour import get_flavour
from et_pipeline.transform_3NF_product_size import get_product_size

def get_product_name(basket_item:str) -> str:
    full_product_name = basket_item.split('-')[0].strip()
    product_name_list = full_product_name.replace('Flavoured ','').split(' ')[1:]
    if len(product_name_list) > 1: product_name = ' '.join(product_name_list)
    else: product_name = product_name_list[0]
    return product_name.title()

def get_product_price(basket_item:str) -> float:
    return float(basket_item.strip().split(' ')[-1].strip())

def product_normalised(df: pd.DataFrame, df_product_size: pd.DataFrame, df_product_flavour: pd.DataFrame) -> pd.DataFrame:
    s_product: pd.Series = df['basket_items']
    s_product = s_product.apply(lambda x: x.split(','))
    s_product = s_product.explode()
    
    # Transform data to create new columns (product_name and product_price)
    # Transform data to setup foreign key constraint
    df_product = pd.DataFrame()
    df_product['product_name'] = s_product.apply(get_product_name)
    df_product['product_size_name'] = s_product.apply(get_product_size)
    df_product['product_flavour_name'] = s_product.apply(get_flavour)
    df_product['product_price'] = s_product.apply(get_product_price)
    
    # Create product dataframe by merging with other dataframe to setup constraint with foreign key and by droping unnecessary columns.
    df_product = pd.merge(df_product,df_product_size,on='product_size_name', how='left')
    df_product = pd.merge(df_product,df_product_flavour,on='product_flavour_name', how='left')
    
    df_product = df_product.drop(columns=['product_size_name','product_flavour_name'])
    df_product = df_product.drop_duplicates()
    
    # Hashing columns and applying to id
    df_product['product_id'] = df_product.astype(str).iloc[:,:].sum(axis=1) # Adding each column as a str into a new column to be used as the base for the ID
    df_product['product_id'] = df_product['product_id'].apply(lambda x: str(hashlib.md5((x.strip()).encode('utf-8')).hexdigest()))
    
    # # If you want to sort the values of the dataframe
    df_product = df_product.sort_values(by=['product_id','product_name','product_size_id','product_flavour_id'],na_position='first')
    df_product = df_product.reset_index(drop=True)
    
    df_product = df_product[['product_id','product_name','product_size_id','product_flavour_id','product_price']]
    
    return df_product




# Example
# from extract import extract_file
# from transform_sensitive_data import remove_sensitive_data
# from transform_3NF_product_flavour import product_flavour_normalised
# from transform_3NF_product_size import product_size_normalised
# df = extract_file('chesterfield.csv')
# df = remove_sensitive_data(df,['card_number'])
# df_product_size = product_size_normalised(df)
# df_product_flavour = product_flavour_normalised(df)
# df = product_normalised(df, df_product_size, df_product_flavour)

# print(df.head(12))
