#Check Subset
#https://www.hackerrank.com/challenges/py-check-subset/problem

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        set_n = set(map(int, input().split()))
        m = int(input())
        set_m = set(map(int, input().split()))
        print(set_n.issubset(set_m))
