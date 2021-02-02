from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

print(spark)
rdd = spark.sparkContext.parallelize([1,2,3,4,56])
print("RDD count: ", rdd.count())