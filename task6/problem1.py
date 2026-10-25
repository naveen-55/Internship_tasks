#Python If-Else
#https://www.hackerrank.com/challenges/py-if-else/problem

#!/bin/python3

import math
import os
import random
import re
import sys


def classificator(n):
    if (1 <= n <= 100) and (n % 2 != 0):
        print('Weird')
    elif 2 <= n <= 5:
        print('Not Weird')
    elif 6 <= n <= 20:
        print('Weird')
    elif 20 < n <= 100:
        print('Not Weird')
    else:
        print('Not a valid number')


if __name__ == '__main__':
    n = int(input().strip())
    
    classificator(n)
