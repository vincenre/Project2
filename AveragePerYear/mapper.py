#!/usr/bin/env python
"""mapper.py"""

import sys

for line in sys.stdin: 
    lineList = line.split(",")
    day = lineList[1].strip()
    temp = lineList[3].strip()
    qFlag = lineList[5].strip()
    if qFlag == "":
        if lineList[2].strip() == "TMIN":
            print("%s %s %s" % (day[0:4], temp, "NA"))
        elif lineList[2].strip() == "TMAX":
            print("%s %s %s" % (day[0:4], "NA", temp))
        
   

        
