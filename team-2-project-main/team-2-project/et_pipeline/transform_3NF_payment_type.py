import pandas as pd
import hashlib

def payment_type_normalised(df: pd.DataFrame) -> pd.DataFrame:
    s_payment_type: pd.Series = df['payment_type_name']
    s_payment_type = s_payment_type.drop_duplicates()
    s_payment_type = s_payment_type.reset_index(drop=True)
    
    # Transforming series to DataFrame
    df_payment_type: pd.DataFrame = s_payment_type.to_frame().reset_index()
    df_payment_type = df_payment_type.rename(columns= {'index':'payment_type_id'}) # Changing index name to id table
    
    df_payment_type['payment_type_id'] = df_payment_type['payment_type_name'].apply(lambda x: hashlib.md5((x.strip()).encode('utf-8')).hexdigest()) # Hashing name and applying to id
    
    df_payment_type = df_payment_type[['payment_type_id','payment_type_name']]
    
    return df_payment_type




# Example
# from extract import extract_file
# from transform_sensitive_data import remove_sensitive_data
# df = extract_file('chesterfield.csv')
# df = remove_sensitive_data(df,['card_number'])
# df = payment_type_normalised(df)

# print(df.head())
