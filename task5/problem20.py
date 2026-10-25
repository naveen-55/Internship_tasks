#Piling Up!
#https://www.hackerrank.com/challenges/piling-up/problem

def piling_up(cubes):
    left = 0
    right = len(cubes) - 1
    top = float('inf')
    
    while left <= right:
        if cubes[left] >= cubes[right]:
            if cubes[left] > top:
                return "No"
            top = cubes[left]
            left += 1
        else:
            if cubes[right] > top:
                return "No"
            top = cubes[right]
            right -= 1
    
    return "Yes"

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        cubes = list(map(int, input().split()))
        print(piling_up(cubes))
