#!/usr/bin/env python
"""mapper.py"""

import sys

current_weatherStation = None
current_year = None
tmin = 0
tmax = 0

#mapper
for line in sys.stdin: 
    lineList = line.split(",")
    weatherStation = lineList[0].strip()
    year = lineList[1].strip()
    temp = lineList[3].strip()
    qFlag = lineList[5].strip()
    
    if current_weatherStation == None:
        current_weatherStation = weatherStation
        current_year = year
        
    if current_weatherStation != weatherStation:
        print("%s %s %s %s" % (current_year[0:4], current_weatherStation, tmin, tmax))
        current_weatherStation = weatherStation
        current_year = year
        tmin = 0
        tmax = 0
        
    if qFlag == "":
        if lineList[2].strip() == "TMIN":
            tmin = temp
        elif lineList[2].strip() == "TMAX":
            tmax = temp
