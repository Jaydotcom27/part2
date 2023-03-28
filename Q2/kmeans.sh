#!/bin/sh
../../start.sh

/usr/local/hadoop/bin/hdfs dfs -rm -r /part2/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /part2/matrix/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/hdfstest2/shot_logs.csv /part2/matrix/input/

# Compute the averages per player for {SHOT DIST, CLOSE DEF DIST, SHOT CLOCK}
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file mapper1.py -mapper mapper1.py \
-file reducer1.py -reducer reducer1.py \
-input /part2/matrix/input/* -output /part2/matrix/output/

# Mapreduce job to randomly pick 4 initial centroids from data
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file centroids_mapper.py -mapper centroids_mapper.py \
-file centroids_reducer.py -reducer centroids_reducer.py \
-input /part2/matrix/output/* -output /part2/centroids/output/

readarray -t centroids < <(/usr/local/hadoop/bin/hdfs dfs -cat /part2/centroids/output/*)

# COUNT=0
# ITER=0

# while [ $ITER -lt 15 ]
# do
#     # Clear output folder for next iteration
#     /usr/local/hadoop/bin/hdfs dfs -rm -r /part2/new_centroids/output/

#     #Convert centroids array into string separated by ";" for mapper2.py
#     formatted_centroids=$(python3 format_centroid.py "${centroids[@]}")

#     echo "******************** Getting new centroids ********************"
#     # Mapreduce job to compute new clusters from an initial set of centroids
#     # Mapper: map each player features to its respective cluster, outputs ---> key=cluster_id, value={SHOT DIST, CLOSE DEF DIST, SHOT CLOCK}
#     # Reducer: compute the new centroid values, outputs a line for each k ---> key=cluster_id, value={SHOT DIST, CLOSE DEF DIST, SHOT CLOCK}
#     /usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
#     -file mapper2.py -mapper "mapper2.py $formatted_centroids" \
#     -file reducer2.py -reducer reducer2.py \
#     -input /part2/matrix/output/* -output /part2/new_centroids/output/

#     readarray -t new_centroids < <(/usr/local/hadoop/bin/hdfs dfs -cat /part2/new_centroids/output/*)

#     echo "******************** checking convergence ********************"
#     for (( i=0; i<${#centroids[@]}; i++ ))
#     do
#         read -a old_line <<< "${centroids[$i]}"
#         read -a new_line <<< "${new_centroids[$i]}"
#         echo "old --> ${old_line[1]}"
#         echo "nwe --> ${new_line[1]}"
#         EQUAL=$(python3 check_centroids.py ${old_line[1]} ${new_line[1]})
#         COUNT=$(($COUNT+$EQUAL ))
#     done
#     centroids=("${new_centroids[@]}")
#     ITER=$(( $ITER + 1))
#     echo "ITERATION=$ITER ---> $COUNT"
#     if [ $COUNT == 4 ]
#     then
#         echo "******************** Centroids didn't change ********************"
#         break
#     else
#         COUNT=0
#     fi
# done
# echo "DONE! $ITER iterations"

# echo "******************** Final clusters ********************"
# /usr/local/hadoop/bin/hdfs dfs -cat /part2/new_centroids/output/*


# # Mapreduce job to find zone  for James Harden, Chris Paul, Stephen Curry and Lebron James
# # Mapper: map each player features to its respective cluster, outputs ---> key=player, value=cluster
# # Reducer: Do nothing.. just print ---> key=player, value=cluster
# /usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
# -file player_mapper.py -mapper "player_mapper.py $formatted_centroids" \
# -file player_reducer.py -reducer player_reducer.py \
# -input /part2/matrix/output/* -output /part2/players/output/

# /usr/local/hadoop/bin/hdfs dfs -cat /part2/players/output/*

/usr/local/hadoop/bin/hdfs dfs -rm -r /part2/

../../stop.sh
