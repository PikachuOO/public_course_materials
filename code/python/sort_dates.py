#!/usr/bin/python

import re
from random import randint

def random_date():
    return "%02d/%02d/%04d"%(randint(1,28), randint(1,12), randint(2000,2020))

def parse_date(date1):
    (day, month, year) = re.split(r'\D+', date1)
    return (year, month, day)

random_dates = [random_date() for x in range(0,5)]
print("random_dates: " + ','.join(random_dates))
sorted_dates = sorted(random_dates, key=parse_date)
print("sorted dates: " + ','.join(sorted_dates))