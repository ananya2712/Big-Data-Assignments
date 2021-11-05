from pyspark.sql import SparkSession
import sys
import pyspark.sql.functions as f
from pyspark import SparkContext
from pyspark.sql.types import FloatType

cityPath = sys.argv[1]
globalPath = sys.argv[2]

spark_context = SparkContext.getOrCreate()

spark = SparkSession.builder.master("local").appName("task1").getOrCreate()
city_file = spark.read.csv(cityPath, inferSchema = True, header = True)
global_file = spark.read.csv(globalPath, inferSchema = True, header = True)

city_file.AverageTemperature = city_file.AverageTemperature.cast(FloatType())
global_file.LandAverageTemperature = global_file.LandAverageTemperature.cast(FloatType())

columns = ['dt','Country']

avg_temp_country = city_file.groupBy(columns).agg(f.max("AverageTemperature"))
avg_temp_country = avg_temp_country.withColumnRenamed("max(AverageTemperature)","average")

ans = avg_temp_country.join(global_file,[ avg_temp_country.average > global_file.LandAverageTemperature , avg_temp_country.dt == global_file.dt ])

ans2 = ans.filter(avg_temp_country['average'] > global_file['LandAverageTemperature'])
	
collectedDF = ans2.groupBy(avg_temp_country.Country).count().orderBy(f.asc(avg_temp_country.Country)).collect()

for row in collectedDF:
	print(row['Country'] + '\t' + str(row['count']))

