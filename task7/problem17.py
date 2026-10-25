#Separate the Numbers
#https://www.hackerrank.com/challenges/separate-the-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    for i in range(len(s)//2):
        n = s[:(i+1)]
        l = 0
        while l < len(s):
            t = str(int(n)+1)
            if s.find(t,l) != -1 :
                if s.find(n,l) + len(n) != s.find(t,l) :
                    break
                else :
                    l += len(n)
                    n = t
            else:
                l += len(n)
                break
        if l == len(s):
            print(f'YES {s[:(i+1)]}')
            return
    else :
        print('NO')
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
