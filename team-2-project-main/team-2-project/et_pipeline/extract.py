import pandas as pd

def extract_file(filename: str) -> pd.DataFrame:
    try:
        # Extract csv file into a pandas DataFrame
        extract_file_df = pd.read_csv(filename, names=["timestamp", "store_name", "customer_name", "basket_items", "total_price", "payment_type_name", "card_number"])
    except:
        return None
    return extract_file_df


# Example
# df = extract_file("chesterfield.csv")
# print(df.head())
# print(pd.Series(df.fillna('').values.tolist(), index=df.index).str.join(''))
