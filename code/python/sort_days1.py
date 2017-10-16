#!/usr/bin/python

import random

day_names = "Sunday Monday Tuesday Wednesday Thursday Friday Saturday"
days = dict(list(zip(day_names.split(), list(range(0,7)))))

random_days = [random.choice(list(days.keys())) for x in range(0,5)]
print("random_days = " + ','.join(random_days))

sorted_days = sorted(random_days, key=lambda x:days[x])
print("sorted_days = " + ','.join(sorted_days))
