Description:
This project contains a fully vertical scalable ETL (Extract, Transform, Load) pipeline to handle large volumes of transaction data for our client (T2 Cafe Franchise Manager). Unlike the individual mini-project, our serverless application allows our client to:

Access real data from over 100 cafe locations;
Identify local and regional customer trends;
Use this information to make informed and impactful decisions.
Technologies & Architectures:
Languages: Python 3.8, Yaml, SQL
Cloud Provider: AWS
Storage: Amazon S3
Compute: AWS Lambda
Integration Amazon SQS
Database Amazon Redshift
Parameter/Password store - AWS SSM
Access Control - AWS IAM
Analytics & Monitoring: Grafana, AWS CloudWatch
Source Control CI/CD Pipeline, Git
Schema Design Draw.io Link to our Serverless Event Driven ETL Pipeline
Unit Testing:
Unit tests are written with the use of the Pandas Libary pandas.test, and Python's built in libraries such as Pytest and Moto. The transformation for 3NF for each table is fully unit tested.

How it Works:
The ETL process (Extract, Transform, Load) allows data to be gathered from multiple sources and consolidated into a single, centralized location. 100+ CSV files are dropped into a S3 Bucket 8pm daily. A CloudWatch Event rule is used to automate the configured ETL process. The function is triggered when new data files are being uploaded, and then the raw data is then transformed and cleaned using AWS Lambda
Python Package boto3 is used to extract raw CSV data from an S3 bucket.
The raw data is then transformed and cleaned, using Amazon Simple Queue Service (SQS) message system and the Lambda resource: Event Source Mapping, it then triggers the decoupled 'Load Lambda Function'.
The Python Package psycopg2 is used to load this transformed data to a relational Redshift Database.
