# Find the number of times where a city’s average temperature on a day turned out to be higher than the city’s average temperature throughout the dataset for a given country.

from pyspark.sql import SparkSession
import sys
import pyspark.sql.functions as f
# import org.apache.spark.sql.functions._

country = sys.argv[1]
path = sys.argv[2]

spark = SparkSession.builder.master("local").appName("task1").getOrCreate()
city_file = spark.read.csv(path, inferSchema = True, header = True)

if "Country" in city_file.columns:
	avg_temp = city_file.where(f.col("Country") == country).groupBy("City").agg(f.avg("AverageTemperature"))
	avg_temp = avg_temp.withColumnRenamed("avg(AverageTemperature)","average")
	country = city_file.where(f.col("Country") == country)
	
	ans = country.join(avg_temp,[ country.AverageTemperature > avg_temp.average , country.City == avg_temp.City ])
	# print(ans.groupBy(country.City).count().collect())
	
	collectedDF = ans.groupBy(country.City).count().orderBy(f.asc(country.City)).collect()
	for row in collectedDF:
		print(row['City'] + '\t' + str(row['count']))
