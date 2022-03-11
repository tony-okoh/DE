import pandas as pd
import hashlib
def store_normalised(df: pd.DataFrame) -> pd.DataFrame:
    s_store: pd.Series = df['store_name']
    s_store = s_store.drop_duplicates()
    s_store = s_store.reset_index(drop=True)
    
    # Transforming series to DataFrame
    df_store: pd.DataFrame = s_store.to_frame().reset_index()
    df_store = df_store.rename(columns= {'index':'store_id'}) # Changing index name to id table
    df_store['store_id'] = df_store['store_name'].apply(lambda x: hashlib.md5((x.strip()).encode('utf-8')).hexdigest())
    
    df_store = df_store[['store_id','store_name']]
    
    return df_store

# Example
# from extract import extract_file
# from transform_sensitive_data import remove_sensitive_data
# df = extract_file('chesterfield.csv')
# df = remove_sensitive_data(df,['card_number'])
# df = store_normalised(df)

# print(df.head())
