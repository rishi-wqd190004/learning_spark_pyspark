from pyspark.sql import SparkSession
from pyspark import SQLContext

spark = SparkSession.builder.appName('spark_learning').getOrCreate() # sets a name for th eapplication and can be seen in Spark Web UI

print(spark)
rdd = spark.sparkContext.parallelize([1,2,3,4,56])
print("RDD count: ", rdd.count())

## creating rdd using parallelize()
dataList = [('Java', 20000), ('Python', 100000), ('Scala', 3000)]
rdd = spark.sparkContext.parallelize(dataList)
print('RDD count parallelize: ', rdd.count())

## creating rdd using external file here textFile()
# rdd2 = spark.sparkContext.textFile('/home/richie/kaggle_datasets/5e15730aa280850006f3d005.txt')
# print('RDD line count textfile: ', rdd2.count())
# # get count of Wifi and gyroscope used in lines
# num_wifi = rdd2.filter(lambda s: 'WIFI' in s).count()
# num_gyro = rdd2.filter(lambda s: 'GYROSCOPE' in s).count()
# print('lines with wifi: {}, lines with GYROSCOPE: {}'.format(num_wifi, num_gyro))

## you can create new_RDD from the existing RDD

## RDD Operations
## RDD Transformation
# flatmap transformation
# rdd2_1 = rdd2.flatMap(lambda x: x.splitlines(True))
# for element in rdd2_1.collect():
#     with open('/home/richie/kaggle_datasets/dump_data.txt', 'a') as f:
#         f.writelines(element)
# # count action
# print("RDD count: ", rdd2_1.count())

# another example
data=[("Z", 1),("A", 20),("B", 30),("C", 40),("B", 30),("B", 60)]
inputRDD = spark.sparkContext.parallelize(data)
listRDD = spark.sparkContext.parallelize([1,2,3,4,5,3,2]) # here created 2 RDD's
## aggregate action
seqOp = (lambda x,y: x+y)
combOp = (lambda x,y: x+y)
agg = listRDD.aggregate(0, seqOp, combOp)
print(agg)
# another
seqOp2 = (lambda x, y: (x[0] + y, x[1] + 1))
combOp2 = (lambda x, y: (x[0] + y[0], x[1] + y[1]))
agg2 = listRDD.aggregate((0, 0), seqOp2, combOp2)
print(agg2)