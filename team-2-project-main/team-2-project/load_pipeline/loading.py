import logging

from load_pipeline.database_manager import create_connection, execute_query

# Set up variables
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

# Create temporary table with unique name
def create_temp_table(con, temp_table_name: str, parent_table: str) -> None: 
    sql_query = (f"CREATE TEMP TABLE {temp_table_name} "
                f"(LIKE cafe_data.{parent_table});")

    execute_query(con, sql_query)    

# Fill temporary table with new data from the file that triggered SQS
def copy_to_table(con, temp_table_name: str, load_bucket_name: str, filename: str, arn_iam_redshift_role: str) -> None:
    sql_query = (f"COPY {temp_table_name} FROM 's3://{load_bucket_name}/{filename}' "
                f"iam_role '{arn_iam_redshift_role}' REGION 'eu-west-1' "
                f"CSV timeformat 'YYYY-MM-DD HH24:MI:SS' ignoreheader as 1;")
    execute_query(con, sql_query)

# Merge temp and parent table, and enforcing primary column's records to be unique. Closes the cursor after executing the query.
def merge_tables(con, parent_table: str, temp_table_name: str, p_key_column_name: str) -> None:
    sql_query = (f"INSERT INTO cafe_data.{parent_table} "
                f"SELECT t.* FROM {temp_table_name} t "
                f"LEFT JOIN cafe_data.{parent_table} p ON p.{p_key_column_name} = t.{p_key_column_name} "
                f"WHERE p.{p_key_column_name} IS NULL;")

    execute_query(con, sql_query, close_cursor=True)

# Get the name of the primary key column
def get_pkey(parent_table: str) -> str: 
    if parent_table == 'orders':            return 'order_id'
    if parent_table == 'customer':          return 'customer_id'
    if parent_table == 'store':             return 'store_id'
    if parent_table == 'product':           return 'product_id'
    if parent_table == 'product_size':      return 'product_size_id'
    if parent_table == 'product_flavour':   return 'product_flavour_id'
    if parent_table == 'payment_type':      return 'payment_type_id'
    if parent_table == 'order_item':        return 'order_item_id'

def load_to_redshift(filename: str, parent_table: str, load_bucket_name: str) -> None:
    # Set up variables
    arn_iam_redshift_role = 'arn:aws:iam::696036660875:role/RedshiftS3Role'
    temp_table_name = filename[:-4].replace('-','_').replace('/', '_')
    
    # Creating a connection to redshift
    con = create_connection()
    
    # Create temporary table like parent table
    create_temp_table(
        con=con,
        temp_table_name=temp_table_name,
        parent_table=parent_table)
    
    # Fill temporary table with new data
    copy_to_table(con=con,
        temp_table_name=temp_table_name,
        load_bucket_name=load_bucket_name,
        filename=filename,
        arn_iam_redshift_role=arn_iam_redshift_role)    
    
    # Get primary key
    p_key_column_name = get_pkey(parent_table)
    
    # Merge the temp and parent table, enforcing the primary key while doing so
    merge_tables(
        con=con,
        parent_table=parent_table,
        temp_table_name=temp_table_name,
        p_key_column_name=p_key_column_name)
    
    # Close connection
    con.close() 
