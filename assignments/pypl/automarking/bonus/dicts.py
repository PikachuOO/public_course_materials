#!/usr/bin/python3
# 5059649
outer_dict = {}
outer_dict[0] = {}
outer_dict[0][1] = "one"
outer_dict[0][2] = "two"
for key in sorted(outer_dict[0].keys()):
    print(outer_dict[0][key])
