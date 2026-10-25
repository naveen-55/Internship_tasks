#Text Wrap
#https://www.hackerrank.com/challenges/text-wrap/problem
import textwrap

def wrap(string, max_width):
    newstring = ''
    i = 0
    while i < len(string) and i + max_width < len(string):
        newstring = newstring + string[i : i + max_width] + '\n'
        i += max_width
    newstring = newstring + string[i:] + '\n'
    return newstring

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
