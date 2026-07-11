"""Apache Spark SQL connector using PySpark."""

import os

from pyspark.sql import SparkSession


def connect() -> SparkSession:
    """Create and return a Spark SQL session.

    Environment Variables:
        SPARK_APP_NAME: Spark application name (default: SparkSQL)
        SPARK_MASTER: Spark master URL (default: local[*])
    """
    app_name = os.environ.get('SPARK_APP_NAME', 'SparkSQL')
    master = os.environ.get('SPARK_MASTER', 'local[*]')

    spark = SparkSession.builder \
        .appName(app_name) \
        .master(master) \
        .getOrCreate()
    return spark


if __name__ == "__main__":
    try:
        spark = connect()
        print(f"Spark version: {spark.version}")
        spark.stop()
    except Exception as e:
        print(f"Failed to connect to Spark SQL: {e}")
