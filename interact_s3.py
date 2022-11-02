import boto3
import pandas as pd

#Criar um cliente para interagir com o AWS S3
s3_client = boto3.client('s3')

s3_client.download_file("datalake-fecarotta-igti-edc",
                        "data/meses.csv",
                        "meses.csv")

df = pd.read_csv("meses.csv", sep=";")
print(df)