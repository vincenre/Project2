#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys


current_year = None
current_count = 0
year = None
gTmin = 0
gTmax = 0

for line in sys.stdin:
    line = line.strip()
    year, tmin, tmax, count = line.split(' ',3)
    year = year.strip()
    tmin = tmin.strip()
    tmax = tmax.strip()
    count = count.strip()
    try:
        count = int(count)
    except ValueError:

        continue
    if current_year == year:
        current_count += count
        if tmin != "NA":
            gTmin += float(tmin)
        else:
            gTmax += float(tmax)
    else:
        if current_year:
	    if gTmin != 0 and gTmax != 0:
                current_count = current_count/2
		avgTmin = gTmin/ float(current_count)
		avgTmax = gTmax/ float(current_count)
		print ( '%s\t%s\t%s' % (current_year, avgTmin, avgTmax))
	gTmin = 0
	gTmax = 0
        current_count = count
        current_year = year

if current_year == year:
    if gTmin != 0 and gTmax != 0:
        current_count = current_count/2
	avgTmin = gTmin/ float(current_count)
	avgTmax = gTmax/ float(current_count)
	print ( '%s\t%s\t%s' % (current_year, avgTmin, avgTmax)) 
        


