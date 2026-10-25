#String Formatting
#https://www.hackerrank.com/challenges/python-string-formatting/problem
def print_formatted(number):
    # your code goes here
    bin_n = f'{number:b}'
    width = len(bin_n)+1 #width of the largest binary number + 1 space
    
    for i in range(1, n+1):
        print(f'{i}'.rjust(width-1), end = '') #first column will not have space
        print(f'{i:o}'.rjust(width), end = '') #:o for octal
        print(f'{i:X}'.rjust(width), end = '') #:X for hexadecimal
        print(f'{i:b}'.rjust(width)) #:b for binary


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
