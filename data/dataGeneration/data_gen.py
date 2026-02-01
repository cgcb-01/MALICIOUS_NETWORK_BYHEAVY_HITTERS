from pyspark.sql import SparkSession
def generate_data(freq_threshold,call_status_count,timestamp_out_count):
    spark=SparkSession.builder.appName("DataGeneration").getOrCreate()