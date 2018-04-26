#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys


current_year = None
year = None
stationsTemp = []

for line in sys.stdin:
    line = line.strip()
    year, weatherstation, tmin, tmax = line.split(' ',3)
    
    year = year.strip()
    weatherstation = weatherstation.strip()
    tmin = tmin.strip()
    tmax = tmax.strip()
    
    if current_year == year:
        temp = (year, weatherstation, int(tmin), int(tmax))
        stationsTemp.append(temp)
    else:
        if len(stationsTemp) > 0:
            sortedStations = sorted(stationsTemp, key=lambda st:st[1])
            avgStations = []
            current_station = None
            count = 0
            tmin = 0
            tmax = 0
            for i in range(0,len(stationsTemp)):
                if current_station == None:
                    current_station = sortedStations[i][1]
                    
                if current_station == sortedStations[i][1]:
                    tmin += int(sortedStations[i][2])
                    tmax += int(sortedStations[i][3])
                    count += 1
                else :
                    tmin = tmin/count
                    tmax = tmax/count
                    avgStations.append((sortedStations[i][0], current_station, tmin, tmax))
                    tmin = int(sortedStations[i][2])
                    tmax = int(sortedStations[i][3])
                    count = 1
                    current_station = sortedStations[i][1]
                    
            sortedStationsTmin = sorted(avgStations, key=lambda st:st[2])
            sortedStationsTmax = sorted(avgStations, key=lambda st:st[3], reverse=True)    
            print("5 Hottest Stations for %s" % avgStations[0][0])
            for i in range(0,5):
                print ( '%s\t%s' % (sortedStationsTmax[i][1], sortedStationsTmax[i][3]))
            print("5 Coldest Stations for %s" % avgStations[0][0])
            for i in range(0,5):
                print ( '%s\t%s' % (sortedStationsTmin[i][1], sortedStationsTmin[i][2]))
        current_year = year
        stationsTemp = []

if current_year == year:
    if len(stationsTemp) > 0:
        sortedStations = sorted(stationsTemp, key=lambda st:st[1])
        avgStations = []
        current_station = None
        count = 0
        tmin = 0
        tmax = 0
        for i in range(0,len(stationsTemp)):
            if current_station == None:
                current_station = sortedStations[i][1]
                
            if current_station == sortedStations[i][1]:
                tmin += int(sortedStations[i][2])
                tmax += int(sortedStations[i][3])
                count += 1
            else :
                tmin = tmin/count
                tmax = tmax/count
                avgStations.append((sortedStations[i][0], current_station, tmin, tmax))
                tmin = int(sortedStations[i][2])
                tmax = int(sortedStations[i][3])
                count = 1
                current_station = sortedStations[i][1]
                
        sortedStationsTmin = sorted(avgStations, key=lambda st:st[2])
        sortedStationsTmax = sorted(avgStations, key=lambda st:st[3], reverse=True)    
        print("5 Hottest Stations for %s" % avgStations[0][0])
        for i in range(0,5):
            print ( '%s\t%s' % (sortedStationsTmax[i][1], sortedStationsTmax[i][3]))
        print("5 Coldest Stations for %s" % avgStations[0][0])
        for i in range(0,5):
            print ( '%s\t%s' % (sortedStationsTmin[i][1], sortedStationsTmin[i][2]))
            


