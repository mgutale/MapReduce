#! /usr/bin/env python3

# import libraries
import sys
from collections import defaultdict


# define required functions - mean, median and variance
def mean(array):
    """define mean function"""
    N = len(array)  # number of observations
    return sum(array) / N


def median(array):
    """define median function"""
    sortedarray = sorted(array)
    arraylen = len(array)
    index = (arraylen - 1) // 2

    if arraylen % 2:
        return sortedarray[index]
    else:
        return (sortedarray[index] + sortedarray[index + 1]) / 2.0


def variance(array):
    """define variance functions using the mean above"""
    N = len(array)  # number of observations
    return sum([(i - mean(array)) ** 2 for i in array]) / N


# Define an empty dictionary to store keys and values
data = defaultdict(list)
# Loop through the dictionary and print the max, min and variance for each day.
for values in sys.stdin:
    day, temp = values.strip(' ').split('\t')
    if '-\n' not in temp:
        data[day].append(int(temp))

# calculate the statistics
print('YearMonthDay', ',', 'Min Dry Bulb Temp', ',', 'Max Dry Bulb Temp', ',', 'Mean Dry Bulb Temp', ',',
      'Median Dry Bulb Temp', ',', 'Variance Dry Bulb Temp')
for key, value in data.items():
    print('{},{},{},{:.2f},{:.2f},{:.2f}'.format(key, min(value), max(value), mean(value), median(value),
                                                 variance(value)))
