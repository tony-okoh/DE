import logging
import boto3
from load_pipeline.loading import load_to_redshift
import json

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)
s3_client = boto3.client('s3')

def handler(event, context):
    LOGGER.info(f'Event structure: {event}')
    
    bucket_name = json.loads(event['Records'][0]['body'])['Records'][0]['s3']['bucket']['name']
    key_name = json.loads(event['Records'][0]['body'])['Records'][0]['s3']['object']['key']
    LOGGER.info(f"Record length in data bucket: {len(event['Records'])}")
    LOGGER.info('New dataframe in load bucket.')
    LOGGER.info(f'{bucket_name = }')
    LOGGER.info(f'{key_name = }')
    
    # Process the object through the Loading process
    df_table_name:str = key_name.split('-')[0]
    load_to_redshift(filename=key_name,
                         parent_table=df_table_name,
                         load_bucket_name=bucket_name)
    LOGGER.info(f"Loaded {df_table_name} data")
