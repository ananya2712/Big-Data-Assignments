# Find the number of times where a city’s average temperature on a day turned out to be higher than the city’s average temperature throughout the dataset for a given country.
from pyspark.sql import SparkSession
# from pyspark.sql.functions import col
# import org.apache.spark.sql.functions._
import sys
import pyspark.sql.functions as f

country = sys.argv[1]
path = sys.argv[2]

spark = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate()

city_file = spark.read.csv(path, inferSchema = True, header = True)
rdd = spark.sparkContext.parallelize(city_file)

if "Country" in rdd.columns:
	rdd1 = rdd.where(f.col("Country") == country).groupBy("City").agg(f.avg("AverageTemperature")).collect()
	rdd2 = rdd1.map(lambda x: x.asDict()).collect()
	print(rdd2)
	

