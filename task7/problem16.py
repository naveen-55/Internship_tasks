#Caesar Cipher
#https://www.hackerrank.com/challenges/caesar-cipher-1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    s2 = ''
    for ch in s :
        if ch.isalpha():
            t = ord(ch)
            if 96 <= t <= 122 :
                t += k
                while t > 122 :
                    t -= 26
            elif 65 <= t <= 90 :
                t += k 
                while t > 90 :
                    t -= 26
            s2 += chr(t)
        else :
            s2 += ch
    return s2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
