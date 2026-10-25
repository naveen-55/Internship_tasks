#Gemstones
#https://www.hackerrank.com/challenges/gem-stones/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#

def gemstones(arr):
    # Convert each string to a set of characters
    sets = [set(s) for s in arr]
    
    # Find the intersection of all sets
    common = set.intersection(*sets)
    
    # Return the number of common characters
    return len(common)

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(input().strip())
    result = gemstones(arr)
    print(result)
