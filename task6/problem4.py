#Loops
#https://www.hackerrank.com/challenges/python-loops/problem

def function(n):
    positive_int = [x for x in range(0,n)]
    
    for x in positive_int:
        print(x**2)

if __name__ == '__main__':
    n = int(input())
    function(n)

