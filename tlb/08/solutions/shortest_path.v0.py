#!/usr/bin/python

import sys

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
    min_distance = 1e99  # must be larger than any possible distance
    next_town = ""
    for town in unprocessed_towns:
        if town in shortest_journey and shortest_journey[town] < min_distance:
            min_distance = shortest_journey[town]
            next_town = town

if finish not in shortest_journey:
    print("No route from %s to %s" % (start, finish))
else:
    print("Shortest route is length = %s:%s %s." % (shortest_journey[finish], route[finish], finish))

