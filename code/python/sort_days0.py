#!/usr/bin/python

import random

days = {'Sunday':0, 'Monday':1, 'Tuesday':2, 'Wednesday':3,
         'Thursday':4, 'Friday':5, 'Saturday':6}

def random_day():
    return str(random.choice(list(days.keys())))

def day_number(day):
    return days[day]

random_days = [random_day() for x in range(0,5)]
print("random_days = " + ','.join(random_days))

sorted_days = sorted(random_days, key=day_number)
print("sorted_days = " + ','.join(sorted_days))
