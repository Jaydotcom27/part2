#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /part2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /part2/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /part2/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../data/shot_logs.csv /part2/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file mapper.py -mapper mapper.py \
-file reducer.py -reducer reducer.py \
-input /part2/input/* -output /part2/output/
echo "*********************** most unwanted defender (defender, hit rate, shots againts defender) ********************* "
/usr/local/hadoop/bin/hdfs dfs -cat /part2/output/part-00000
echo "**********************************************************"
/usr/local/hadoop/bin/hdfs dfs -rm -r /part2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /part2/output/
../../stop.sh
