# Project2

### Question 1 : Average TMIN, TMAX for each year excluding abnormalities or missing data

The mapper and reducer for this query is in AveragePerYear Folder

The mapper.py file simply outputs (year, temp, "NA") for TMIN value and (year, "NA", temp) for TMAX for every entry in dataset. The reducer.py file simply puts all these together and gives out the summary.

As I am in Windows and I am using PUTTY, I had to first copy the file onto the HADOOP cluster. I used the following command to copy the files from my local directory to hadoop directory.

> pscp -l vincenre D:\UC\Spring2017\CloudComputing\Project2\AveragePerYear\mapper.py vincenre@hadoop-gate-0.eecs.uc.edu:/home/vincenre/project2

> pscp -l vincenre D:\UC\Spring2017\CloudComputing\Project2\AveragePerYear\reducer.py vincenre@hadoop-gate-0.eecs.uc.edu:/home/vincenre/project2

The command that I used to run the job is :
>hadoop jar /usr/hdp/2.6.3.0-235/hadoop-mapreduce/hadoop-streaming-2.7.3.2.6.3.0-235.jar -file /home/vincenre/project2/mapper.py -mapper
/home/vincenre/project2/mapper.py -file /home/vincenre/project2/reducer.py -reducer /home/vincenre/project2/reducer.py -input /data/weather/* -output /home/vincenre/job1/averageTMINTMAX

### Question 2 : Maximum TMAX, Minimum TMIN for each year excluding abnormalities or missing data

The mapper and reducer for this query is in MaxMinWeather Folder

The mapper.py file simply outputs (year, temp, "NA") for TMIN value and (year, "NA", temp) for TMAX for every entry in dataset. The reducer.py file simply calculates the min of TMIN and min of TMAX for each year.

### Question 3 : 5 hottest , 5 coldest weather stations for each year excluding abnormalities or missing data 

The mapper and reducer for this query is in TopWeatherStations Folder

The mapper.py file simply outputs (year, weatherStation, tmin, tmax) for every entry in dataset. The reducer.py file puts the output of the map function into a list and sorts it. It then calculates the average of the TMIN and TMAX for a particular station. It the sorts the TMIN and TMAX in two lists and outputs the 5 Hottest and 5 Coldest Stations for every year.

#### The Hadoop cluster kept throwing a (physical memory reached) error and was not completing the jobs. So I broke up the job into  4 parts by proving 4-5 input files at a time. 

### Question 4 :  Hottest and coldest day and corresponding weather stations in the entire dataset 

The mapper and reducer for this query is in ColdestHottest Folder

The mapper.py file simply outputs (year, date, weatherstation, tmin ,tmax) for every entry in dataset. The reducer.py file checks the Tmin and Tmax value of every output of a map function and updates the current Tmin and TMax value. A global counter is maintained and when all the input files have been processed, the weather station with lowest and highest temperature is along with the date on which the lowest or highest temperature was recorded is given as the output

