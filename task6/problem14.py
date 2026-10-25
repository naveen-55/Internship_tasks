#Set .intersection() Operation
#https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

if __name__ == '__main__':
    n = int(input())
    set_n = set(map(int, input().split()))
    m = int(input())
    set_m = set(map(int, input().split()))
    print(len(set_n.intersection(set_m)))
