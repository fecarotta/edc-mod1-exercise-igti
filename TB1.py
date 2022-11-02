import boto3
import pandas as pd

#Criar um cliente para interagir com o AWS S3
s3_client = boto3.client('s3')

s3_client.upload_file("data/MICRODADOS_ENEM_2020.csv",
                        "datalake-fecarotta-igti-edc",
                        "data/MICRODADOS_ENEM_2020.csv")