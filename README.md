# NBA Shot data analysis (Part 2)

This repository contains two subfolders answering different questions. 

Q1: looks into finding the "most unwanted defender". Meaning: the player causing the lowest shot success rate when faced by another player.

For this particular case we needed a single Mapper and a single Reduce. In the mapping process we extracted player information from the input csv, did some simple data cleaning and created KVPs with the form `((shooter, defender), (made))`.
The reducing process creates a dictionary and checks the lowest rate of made shots based on the defender.

-----------------------

Q2: looks to classify James Harden, Chris Paul, Stephen Curry and Lebron James into 4 comfortable zones based on where in the court they perform best. 

To answer question #2 the mapping and reduce proccesses are a bit more dense but in a general sense: we created ranged buckets to segment the data, map the information of each player to those blocks and output a tuple with the form `(player, (shot_dist_zone, defender_dist_zone, shot_clock_zone))`
The reduce process compiles the counting and filters out results only for the specified players.

## Getting Started

To get started, clone the repository and ensure that you have Python 3 installed on your machine.

`git clone https://github.com/Jaydotcom27/part2.git`

## Data

The data used in this analysis was obtained from Kaggle, which can be accessed here: https://www.kaggle.com/datasets/dansbecker/nba-shot-logs

## Usage

To run this code you need a functional HDFS system running, for our experiments a 3 node cluster hosted on Google Cloud was the way to go. Two worker nodes and one manager orchestrating.
The driver code is stored in the files `test.sh` and it will run the mappers/reducer to answer all the questions. Make sure to double check the appropiate location for the data csv, it can be found
inside of the driver code where there's a copyFromLocal statement `/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/hdfstest2/shot_logs.csv /part2/input/`. 
This route is expected to be different depending on each system file distribution. 

## Findings

- Q1. James Bernard is the most feared defender with `21.88%` of fear score.
- Q2. Curry -> Bucket 3 | Harden -> Bucket 3 | Paul -> Bucket 3 | Lebron -> Bucket 2


## Conclusion 

Through the use of this MapReduce framework we are able to analyze dense NBA data and draw several conclusions about how players perform. We looked both at defensive and offensive stats.

