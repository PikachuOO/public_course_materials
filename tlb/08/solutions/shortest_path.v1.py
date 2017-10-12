#!/usr/bin/python

import fileinput, re, sys, collections

(start,finish) = sys.argv[1:]
distance = {}
for line in sys.stdin:
    (town1,town2,dist) = line.split()
    distance[(town1,town2)] = int(dist)
    distance[(town2,town1)] = int(dist)

shortest_journey = {start:0}
route = {start:''}
unprocessed_towns = set(d[0] for d in distance.keys())
next_town = start
while next_town and next_town != finish:
    unprocessed_towns.remove(next_town)
    for town in unprocessed_towns:
        if (next_town,town) in distance:
            d = shortest_journey[next_town] + distance[(next_town,town)]
            if town not in shortest_journey or shortest_journey[town] > d:
                shortest_journey[town] = d
                route[town] = route[next_town] + " " + next_town
    next_town = min((shortest_journey[town],town) for town in unprocessed_towns if town in shortest_journey)[1]

if finish not in shortest_journey:
    print("No route from %s to %s" % (start, finish))
else:
    print("Shortest route is length = %s: %s %s." % (shortest_journey[finish], route[finish], finish))

