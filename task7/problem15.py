#Game of Thrones - I
#https://www.hackerrank.com/challenges/game-of-thrones/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    chars = {}

    for c in s:
        if c not in chars:
            chars[c] = 0

        if chars[c] > 0:
            chars[c] -= 1
        else:
            chars[c] += 1
            
    if sum(chars.values()) <= 1:
        return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
