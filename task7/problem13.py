#Sherlock and the Valid String
#https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

from collections import Counter

def isValid(s):
    freq = Counter(s)  # char counts
    freq_values = Counter(freq.values())  # how many chars have same count
    
    # Case 1: all same frequency
    if len(freq_values) == 1:
        return "YES"
    
    # Case 2: only 2 different frequencies
    if len(freq_values) == 2:
        (f1, c1), (f2, c2) = freq_values.items()
        
        # One char occurs once, remove it
        if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
            return "YES"
        
        # One frequency is 1 more than other and occurs once
        if (abs(f1 - f2) == 1) and (c1 == 1 or c2 == 1):
            return "YES"
    
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
