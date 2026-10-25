#Designer Door Mat
#https://www.hackerrank.com/challenges/designer-door-mat/problem

def print_door_mat(n, m):
    # Print the top half
    for i in range(1, n, 2):
        print((i * ".|.").center(m, '-'))

    # Print the middle line
    print("WELCOME".center(m, '-'))

    # Print the bottom half
    for i in range(n-2, 0, -2):
        print((i * ".|.").center(m, '-'))

if __name__ == '__main__':
    n, m = map(int, input().split())
    print_door_mat(n, m)
