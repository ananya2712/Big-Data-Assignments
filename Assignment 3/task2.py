# Find the number of times where a country’s maximum average temperature on a date turned out to be higher than the worldwide land average temperature on the same date.

from pyspark.sql import SparkSession
import sys
import pyspark.sql.functions as f
# import org.apache.spark.sql.functions._
from pyspark.sql.types import FloatType

cityPath = sys.argv[1]
globalPath = sys.argv[2]

spark = SparkSession.builder.master("local").appName("task1").getOrCreate()
city_file = spark.read.csv(cityPath, inferSchema = True, header = True)
global_file = spark.read.csv(globalPath, inferSchema = True, header = True)

city_file.AverageTemperature = city_file.AverageTemperature.cast(FloatType())
global_file.LandAverageTemperature = global_file.LandAverageTemperature.cast(FloatType())

columns = ['dt', 'Country']
avg_temp_country = city_file.groupBy(columns).agg(f.avg("AverageTemperature"))
avg_temp_country = avg_temp_country.withColumnRenamed("avg(AverageTemperature)","average")

ans = avg_temp_country.join(global_file,[ avg_temp_country.average > global_file.LandAverageTemperature , avg_temp_country.dt == global_file.dt ])
	
collectedDF = ans.groupBy(avg_temp_country.Country).count().orderBy(f.asc(avg_temp_country.Country)).collect()

for row in collectedDF:
	print(row['Country'] + '\t' + str(row['count']))

