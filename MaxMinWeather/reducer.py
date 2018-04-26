#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys


current_year = None
year = None
tminArr = []
tmaxArr = []

for line in sys.stdin:
    line = line.strip()
    year, tmin, tmax = line.split(' ',2)
    year = year.strip()
    tmin = tmin.strip()
    tmax = tmax.strip()
    
    if current_year == year:
        if tmin != "NA":
            tminArr.append(int(tmin))
        else:
            tmaxArr.append(int(tmax)) 
    else:
        if current_year:
	   if len(tminArr) > 0 and len(tmaxArr) > 0:
                print ( '%s\t%s\t%s' % (current_year, min(tminArr), max(tmaxArr))) 
        current_year = year
        tminArr = []
        tmaxArr = []

if current_year == year:
    if len(tminArr) > 0 and len(tmaxArr) > 0:
	print ( '%s\t%s\t%s' % (current_year, min(tminArr), max(tmaxArr))) 
        


