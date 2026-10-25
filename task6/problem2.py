#Arithmetic Operators
#https://www.hackerrank.com/challenges/python-arithmetic-operators/problem

def calculator(a,b):
    if (1 <= a <= 10**10) and (1 <= b <= 10**10):
        print(a+b)
        print(a-b)
        print(a*b)
    else:
        print("'a' and/or 'b' not valid")

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    calculator(a,b)

