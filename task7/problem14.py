#Anagram
#https://www.hackerrank.com/challenges/anagram/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

from collections import Counter
def anagram(s):
    len_s = len(s)
    result = -1
    if len_s % 2 == 0:
        l, r = Counter(s[:len_s // 2]), Counter(s[len_s // 2:])
        result = sum((r - l).values())
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
