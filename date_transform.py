#!/usr/bin/env python
from operator import itemgetter
import sys

for line in sys.stdin:
    line = line.strip()
    date_num, count = line.split('\t', 1)

    date_num = int(date_num)

    month = ''
    # Everything is after May
    if 152<date_num and date_num<183:
        month = 'June'
        date_num-=152
    elif 182<date_num and date_num<214:
        month = 'July'
        date_num-=182
    elif 213<date_num and date_num<245:
        month = 'August'
        date_num-=213
    elif 243<date_num and date_num<275:
        month = 'September'
        date_num-=243

    date_string = month + ' ' + str(date_num)
    print "{date}\t{count}".format(date=date_string,count=count)