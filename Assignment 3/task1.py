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

if "Country" in city_file.columns:
	avg_temp = city_file.where(f.col("Country") == country).groupBy("City").agg(f.avg("AverageTemperature")).collect()
	d = avg_temp[0].asDict()
	avg_dict = [{r['City']: r['avg(AverageTemperature)']} for r in avg_temp]
	# print(avg_dict)

c = city_file.where(f.col("Country") == country)
greater = c.agg(f.count(f.when(f.col("AverageTemperature")> next(item for item in avg_dict if item["City"] == f.col("City"))))).show()
print(greater)
		

