#Beautiful Binary String
#https://www.hackerrank.com/challenges/beautiful-binary-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulBinaryString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING b as parameter.
#

def beautifulBinaryString(b):
    count = 0
    b = list(b)
    for i in range(len(b)-2):
        if b[i:i+3] == ['0','1','0']:
            b[i+2] = '1'
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
