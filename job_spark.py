# Comentario para modificar o arquivo .py:
from pyspark.sql.functions import mean, max, min, col, count
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("ExerciseSpark")
    .getOrCreate()
)

# Ler dados do ENEM 2020
enem = (
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", ";")
    .load("s3://datalake-fecarotta-igti-edc/raw-data/")
)

(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .save("s3://datalake-fecarotta-igti-edc/staging/enem")
)