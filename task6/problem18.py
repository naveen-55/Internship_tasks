#Set Mutations
#https://www.hackerrank.com/challenges/py-set-mutations/problem

if __name__ == '__main__':
    n = int(input())
    set_n = set(map(int, input().split()))
    m = int(input())
    for _ in range(m):
        operation = input().split()[0]
        set_b = set(map(int, input().split()))
        if operation == 'intersection_update':
            set_n.intersection_update(set_b)
        elif operation == 'update':
            set_n.update(set_b)
        elif operation == 'difference_update':
            set_n.difference_update(set_b)
        elif operation == 'symmetric_difference_update':
            set_n.symmetric_difference_update(set_b)
    print(sum(set_n))
