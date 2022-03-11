import logging
import boto3
from etl import etl_pipeline

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

def moving_file_to_rejects(bucket_name:str,key_name:str):
    # Copy object A as object B
    s3_resource.Object(bucket_name, f"rejects/{key_name}").copy_from(CopySource=f"/{bucket_name}/{key_name}")
    # Delete the former object A
    s3_resource.Object(bucket_name,key_name).delete()
    LOGGER.info(f'Moved {key_name} to rejects')

def handler(event, context):
    LOGGER.info(f'Event structure: {event}')
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key_name = event['Records'][0]['s3']['object']['key']
    
    if 'rejects/' in key_name: # Need to be tested
        return
    
    LOGGER.info('New object created in bucket.')
    LOGGER.info(f'{bucket_name = }')
    LOGGER.info(f'{key_name = }')
    
    if key_name[-4:] != '.csv': # Need to be tested
        # File is not csv so put it into another folder, log and return
        LOGGER.error(f'File is not csv.')
        moving_file_to_rejects(bucket_name=bucket_name,key_name=key_name)
        return
    
    obj = s3_client.get_object(Bucket=bucket_name, Key=key_name) 
    etl_response = etl_pipeline(file_name=obj['Body'])
    
    if etl_response: LOGGER.info("ETL PROCESS SUCCESSFUL")
    else:
        LOGGER.error("ETL PROCESS UNSUCCESSFUL.")
        moving_file_to_rejects(bucket_name=bucket_name,key_name=key_name)
