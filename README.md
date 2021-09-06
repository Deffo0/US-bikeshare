# US BikeShare
## Overview
In this project, I make use of Python to explore data related to bike share systems for three major cities in the United States `Chicago`,  `New York City`, and `Washington`. I write code to import the data and answer interesting questions about it by computing descriptive statistics. I also write a script that takes in raw input to create an interactive experience in the terminal to present these statistics.
## What Software Do I Use?
* python 3.9.
* pandas library.
* datetime library.
## The Datasets
Randomly selected data for the first six months of `2017` are provided for all three cities.
All three of the data files contain the same core six (6) columns:

1. Start Time (e.g., 2017-01-01 00:07:57)
1. End Time (e.g., 2017-01-01 00:20:53)
1. Trip Duration (in seconds - e.g., 776)
1. Start Station (e.g., Broadway & Barry Ave)
1. End Station (e.g., Sedgwick St & North Ave)
1. User Type (Subscriber or Customer)
#### The Chicago and New York City files also have the following two columns:

1. Gender
1. Birth Year
## Statistics Computed
#### Popular times of travel (i.e., occurs most often in the start time):

* most common month
* most common day of week
* most common hour of day
#### Popular stations and trip:

* most common start station
* most common end station
* most common trip from start to end (i.e., most frequent combination of start station and end station)
#### Trip duration:

* total travel time
* average travel time
#### User info:

* counts of each user type
* counts of each gender (only available for NYC and Chicago)
* earliest, most recent, most common year of birth (only available for NYC and Chicago
