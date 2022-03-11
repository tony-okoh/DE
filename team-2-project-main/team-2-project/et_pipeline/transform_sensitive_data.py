import pandas as pd
from typing import List

def remove_sensitive_data(df:pd.DataFrame, columns_to_remove:List[str]) -> pd.DataFrame:
    try:
        # Removing columns that countains sensitive data.
        df = df.drop(columns=columns_to_remove)
    except:
        return None
    return df