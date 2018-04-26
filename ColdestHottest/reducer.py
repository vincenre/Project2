#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys


current_year = None
year = None
stationsTemp = []
coldest = ""
hottest = ""
counter = 0
gTmin = 0
gTmax = 0

for line in sys.stdin:
    line = line.strip()
    year, date, weatherstation, tmin, tmax = line.split(' ',4)
    date = date.strip()
    year = year.strip()
    weatherstation = weatherstation.strip()
    tmin = tmin.strip()
    tmax = tmax.strip()
    
    if current_year == year:
        if int(tmin) < gTmin:
            gTmin = int(tmin)
            coldest = (year, weatherstation, int(tmin), int(tmax), date)
        if int(tmax) > gTmax:
            gTmax = int(tmax)
            hottest = (year, weatherstation, int(tmin), int(tmax), date)
    else:
        if coldest != "" and hottest != "":
            if counter >=18:
                print("Coldest day was %s on %s recorded at %s " % (coldest[2], coldest[4], coldest[1]))
                print("Hottest day was %s on %s recorded at %s " % (hottest[3], hottest[4], hottest[1]))
            counter += 1
        current_year = year

if current_year == year:
    if coldest != "" and hottest != "":
        if counter >=18:
            print("Coldest day was %s on %s recorded at %s " % (coldest[2], coldest[4], coldest[1]))
            print("Hottest day was %s on %s recorded at %s " % (hottest[3], hottest[4], hottest[1]))
        counter += 1


