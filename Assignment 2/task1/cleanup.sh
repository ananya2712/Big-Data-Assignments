#!/bin/sh

$HADOOP_HOME/bin/hadoop dfsadmin -safemode leave
hdfs dfs -rm -r /Assignment2/Input
hdfs dfs -rm -r /Assignment2/output
hdfs dfs -rm -r /Assignment2
hdfs dfs -mkdir /Assignment2
hdfs dfs -mkdir /Assignment2/Input
hdfs dfs -mkdir /Assignment2/output
hdfs dfs -put dataset_1percent.txt /Assignment2/Input
chmod +x mapper.py reducer.py
dos2unix mapper.py reducer.py

#hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar -mapper "'/home/pes1ug19cs058/Big Data/Assignment 2/task1/mapper.py'" -reducer "'/home/pes1ug19cs058/Big Data/Assignment 2/task1/reducer.py' '/home/pes1ug19cs058/Big Data/Assignment 2/v'" -input /Assignment2/Input/dataset_1percent.txt -output /Assignment2/output/task-1-output
