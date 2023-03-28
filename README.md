# NBA Shot data analysis (Part 2)

This repository contains two subfolders answering different questions. 

Q1: looks into finding the "most unwanted defender". Meaning: the player causing the lowest shot success rate when faced by another player.

For this particular case we needed a single Mapper and a single Reduce. In the mapping process we extracted player information from the input csv, did some simple data cleaning and created KVPs with the form `((shooter, defender), (made))`.
The reducing process creates a dictionary and checks the lowest rate of made shots based on the defender.

-----------------------

Q2: looks to classify James Harden, Chris Paul, Stephen Curry and Lebron James into 4 comfortable zones based on where in the court they perform best. 

To answer question #2 the mapping and reduce proccesses are a bit more dense because we used a K-Means iterative process with several MapReduce jobs, but in a general sense we look at the players, create buckets for each stat to analyze, generate a random centroid and in typical K-Means fashion iterate while updating the centroids and positioning players in the appropiate groups. This is a very broad explanation but we made sure to include detailed comments through the code to bring more clarity.

## Getting Started

Proceed to clone the repository into the already existing `hdfs-test` directory in our Cloud cluster.

`git clone https://github.com/Jaydotcom27/part2.git`

Also consider cloning some test data into the already existing `hdfs-test-data` in our Cloud cluster.

`https://github.com/Jaydotcom27/hdfstest2`

## Data

The data used in this analysis was obtained from Kaggle, which can be accessed here: https://www.kaggle.com/datasets/dansbecker/nba-shot-logs

## Usage

To run this code you need a functional HDFS system running, for our experiments a 3 node cluster hosted on Google Cloud was the way to go. Two worker nodes and one manager orchestrating.
The driver code is stored in the files `test.sh` for `Q1` and `kmeans.sh` for `Q2` and they will run the mappers/reducers to answer all the questions. Make sure to double check the appropiate location for the data csv, it can be found
inside of the driver code where there's a copyFromLocal statement `/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/hdfstest2/shot_logs.csv /part2/input/`. 
This route is expected to be different depending on each system file distribution. 

## Findings

- Q1. James Bernard is the most feared defender with `21.88%` of fear score.
- Q2. Curry, Jarden and Paul seem to land on the same cluster and Lebron is by himself on cluster 2, this makes sense because the initial three play the point guard (and shooting guard ocassionally) position and it is somewhat safe to say that their play styles are similar, for instance, both Curry and Harden are shooters, because of that we were not surprised to find them in the same cluster. When it comes to Lebron, his playstyle and position are different, as a PF that plays closer to the board once again it makes sense that he was placed in a bucket with a shorter shot distance.  


## Conclusion 

Through the use of this MapReduce framework we are able to analyze dense NBA data and draw several conclusions about how players perform. We looked both at defensive and offensive stats to define the comfort zones for the requested players and discovered some interesting insights.

