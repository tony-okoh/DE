import psycopg2
import boto3
import json

ssm_client = boto3.client('ssm')
parameter_response = json.loads(ssm_client.get_parameter(Name='team2_creds',WithDecryption=True)['Parameter']['Value'])
host = parameter_response['host']
user = parameter_response['user']
password = parameter_response['password']
database = 'team2_cafe'
port = 5439

# Create a connection to redshift using SSM parameters
def create_connection():
    con = psycopg2.connect(
        host=host, 
        dbname=database,
        user=user,
        password=password,
        port=port)
    return con

# Creates a cursor from a connection and execute a SQL query. Can close the cursor when necessary.
def execute_query(con, query: str, close_cursor:bool = False) -> None:
    cursor = con.cursor()
    cursor.execute(query)
    con.commit()
    if close_cursor: cursor.close()
