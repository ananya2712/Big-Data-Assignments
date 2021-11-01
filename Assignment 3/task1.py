# Find the number of times where a city’s average temperature on a day turned out to be higher than the city’s average temperature throughout the dataset for a given country.
from pyspark.sql import SparkSession
import sys
import pyspark.sql.functions as f

country = sys.argv[1]
path = sys.argv[2]

spark = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate()
city_file = spark.read.csv(path, inferSchema = True, header = True)

if "Country" in city_file.columns:
	avg_temp = city_file.where(f.col("Country") == country).groupBy("City").agg(f.avg("AverageTemperature"))
	rdd1 = avg_temp.rdd.map(lambda x: {x[0]: x[1]})
	
	print(avg_temp)
	
