from pyspark.sql import SparkSession

def connect():
    spark = SparkSession.builder \
        .appName("SparkSQL") \
        .master("local[*]") \
        .getOrCreate()
    return spark

if __name__ == "__main__":
    spark = connect()
    print(f"Spark version: {spark.version}")
    spark.stop()
