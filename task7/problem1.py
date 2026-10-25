#Set .symmetric_difference() Operation
#https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

n1 = int(input())
set1 = set(map(int, input().split()))
n2 = int(input())
set2 = set(map(int, input().split()))

result = set1.symmetric_difference(set2)
print(len(result))
