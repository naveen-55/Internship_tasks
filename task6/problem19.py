#Company Logo
#https://www.hackerrank.com/challenges/most-commons/problem

#!/bin/python3

from collections import Counter
def top(s):
    x = Counter(s)
    l = []
    for k,v in x.items():
        l.append((k,v))
    l1 = sorted(l, key = lambda x: (-x[1], x[0]), reverse= False)[:3]
    for i in l1:
         print(*i)

if __name__ == '__main__':
    s = input()
    top(s)