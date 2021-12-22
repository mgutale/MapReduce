#! /usr/bin/env python3

# import libraries
import sys

# Read each line of the input file and subset only the day label and Dry Bulb Temp column and return value seperated
# by tab

for index, line in enumerate(sys.stdin):
    # Skip the first column containing the column labels
    if index == 0:
        continue
    else:
        line = line.strip().split(',')
        print("%s \t %s" % (line[1], line[8]))
