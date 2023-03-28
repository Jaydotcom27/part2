#!/bin/sh
../../start.sh

/usr/local/hadoop/bin/hdfs dfs -rm -r /part2/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /part2/matrix/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/hdfstest2/shot_logs.csv /part2/matrix/input/

# First MapReduce job to compute each average per player > this is done for shot distance, closest defender distance and remaining shot clock time
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file mapper1.py -mapper mapper1.py \
-file reducer1.py -reducer reducer1.py \
-input /part2/matrix/input/* -output /part2/matrix/output/

# Generating 4 random initial centroids
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file centroids_mapper.py -mapper centroids_mapper.py \
-file centroids_reducer.py -reducer centroids_reducer.py \
-input /part2/matrix/output/* -output /part2/centroids/output/

mapfile -t centroids < <(/usr/local/hadoop/bin/hdfs dfs -cat /part2/centroids/output/*) # Outputing to centroids

COUNT=0
STEP=0

# Iterate through the K means algorithm until convergence happens or run out of iterations
while [ $STEP -lt 10 ]
do
    /usr/local/hadoop/bin/hdfs dfs -rm -r /part2/new_centroids/output/

    # Prepare centroids for mapper2
    updated_centroids=$(python3 format_centroid.py "${centroids[@]}")

    echo "------------------------- updating centroids "-------------------------
    /usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
    -file mapper2.py -mapper "mapper2.py $updated_centroids" \
    -file reducer2.py -reducer reducer2.py \
    -input /part2/matrix/output/* -output /part2/new_centroids/output/

    readarray -t new_centroids < <(/usr/local/hadoop/bin/hdfs dfs -cat /part2/new_centroids/output/*)

    echo "------------------------- checking convergence "-------------------------
    for (( i=0; i<${#centroids[@]}; i++ ))
    do
        read -a old_line <<< "${centroids[$i]}"
        read -a new_line <<< "${new_centroids[$i]}"
        echo "old --> ${old_line[1]}"
        echo "nwe --> ${new_line[1]}"
        EQUAL=$(python3 check_centroids.py ${old_line[1]} ${new_line[1]})
        COUNT=$(($COUNT+$EQUAL ))
    done
    centroids=("${new_centroids[@]}")
    STEP=$(( $STEP + 1))
    echo "current_iteration=$STEP ---> $COUNT"
    if [ $COUNT == 4 ]
    then
        echo "No change detected"
        break
    else
        COUNT=0
    fi
done
echo "DONE! $STEP iterations"

echo "------------------------- resulting clusters -------------------------"
/usr/local/hadoop/bin/hdfs dfs -cat /part2/new_centroids/output/*


# Final MapReduce job to position each requested player 
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file player_mapper.py -mapper "player_mapper.py $updated_centroids" \
-file player_reducer.py -reducer player_reducer.py \
-input /part2/matrix/output/* -output /part2/players/output/

/usr/local/hadoop/bin/hdfs dfs -cat /part2/players/output/*

/usr/local/hadoop/bin/hdfs dfs -rm -r /part2/

../../stop.sh
