from pyspark.sql import SparkSession
from pyspark import SparkContext
import sys
import pyspark.sql.functions as f

country = sys.argv[1]
path = sys.argv[2]

spark_context = SparkContext.getOrCreate()
spark = SparkSession.builder.master("local").appName("task1").getOrCreate()
city_file = spark.read.csv(path, inferSchema = True, header = True)

if "Country" in city_file.columns:
	avg_temp = city_file.where(f.col("Country") == country).groupBy("City").agg(f.avg("AverageTemperature"))
	avg_temp = avg_temp.withColumnRenamed("avg(AverageTemperature)","average")
	country = city_file.where(f.col("Country") == country)
	
	ans = country.join(avg_temp,[ country.AverageTemperature > avg_temp.average , country.City == avg_temp.City ])
	
	collectedDF = ans.groupBy(country.City).count().orderBy(f.asc(country.City)).collect()
	for row in collectedDF:
		print(row['City'] + '\t' + str(row['count']))
