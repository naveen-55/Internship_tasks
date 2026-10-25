#Symmetric Difference
#https://www.hackerrank.com/challenges/symmetric-difference/problem
if __name__ == '__main__':
    n = int(input())
    set1 = set(map(int, input().split()))
    m = int(input())
    set2 = set(map(int, input().split()))
    symmetric_diff = sorted(set1.symmetric_difference(set2))
    for item in symmetric_diff:
        print(item)
