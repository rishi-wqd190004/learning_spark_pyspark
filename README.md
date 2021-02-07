# learning_spark_pyspark
This is a repository to learn and share more about pyspark and spark applications for ML and Data Science related.

## RDD
RDD is called as resilient distributed dataset. Mainly its the dataset stored in parallel if few other computers are connected.

## RDD Operations
Mainly on PySpark we have 2 features
    - RDD Transformation
    - RDD Actions
Will discuss about each of them with code example.

## RDD Transformation
These are lazy actions and other words you can say its processing part like 'flatMap(), map(), filter(), etc'
These are mainly 2 types:
    - Narrow Transformation
    - Wider Transformation

## Narrow Transformation
compute data on single partition
functions like map(), mapPartition(), flatMap(), etc
![Narrow-transformation](https://i1.wp.com/sparkbyexamples.com/wp-content/uploads/2019/12/narrow-transformation.png?w=545&ssl=1)
(Source:https://sparkbyexamples.com/apache-spark-rdd/spark-rdd-transformations/) 

## Wider Transformation
compute data from multiple partitions
functions like groupByKey(), aggregateByKey(), join(), etc
![Wider-transformation](https://i0.wp.com/sparkbyexamples.com/wp-content/uploads/2019/12/wider-transformation.png?w=539&ssl=1)
(Source:https://sparkbyexamples.com/apache-spark-rdd/spark-rdd-transformations/)
