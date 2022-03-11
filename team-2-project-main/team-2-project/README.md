#  Team 2 Final Project

### _Description_:  

This project contains a fully vertical scalable ETL (Extract, Transform, Load) pipeline to handle large volumes of transaction data for our client (T2 Cafe Franchise Manager). Unlike the individual mini-project, our serverless application allows our client to:  
1. Access real data from over 100 cafe locations;  
2. Identify local and regional customer trends;  
3. Use this information to make informed and impactful decisions.

### _Technologies & Architectures_:
* **Languages:** Python 3.8, Yaml, SQL<br/> 
* **Cloud Provider:** AWS<br/> 
   * **Storage:** Amazon S3
   * **Compute:** AWS Lambda 
   * **Integration** Amazon SQS
   * **Database** Amazon Redshift
   * **Parameter/Password store** - AWS SSM
   * **Access Control** - AWS IAM
   * **Analytics & Monitoring:** Grafana, AWS CloudWatch <br/>
* **Source Control** CI/CD Pipeline, Git
* **Schema Design** Draw.io <a href="https://cdn.discordapp.com/attachments/933384595389448254/946069652818243694/Schema_Design-Sprint_4_Event_Driven_Architecture.drawio2.png"> Link to our Serverless Event Driven ETL Pipeline </a>



### _Unit Testing_:
Unit tests are written with the use of the Pandas Libary pandas.test, and Python's built in libraries such as Pytest and Moto.
The transformation for 3NF for each table is fully unit tested. 

### _How it Works_:
The ETL process **(Extract, Transform, Load)** allows data to be gathered from multiple sources and consolidated into a
single, centralized location. 100+ CSV files are dropped into a S3 Bucket 8pm daily. A CloudWatch Event rule is used to automate the configured ETL process. The function is triggered when new data files are being uploaded, and then the raw data is then transformed and cleaned using AWS Lambda <br />
Python Package *boto3* is used to extract raw CSV data from an S3 bucket.<br /> 
The raw data is then transformed and cleaned, using Amazon Simple Queue Service (SQS) message system and the Lambda resource: Event Source Mapping, it then triggers the decoupled 'Load Lambda Function'.<br />
The Python Package *psycopg2* is used to load this transformed data to a relational Redshift Database.<br />



