#Find a String
#https://www.hackerrank.com/challenges/find-a-string/problem
def count_substring(string, sub_string):
    index_appear = set()
    for i in range(0,len(string)):
        index_appear.add(string.find(sub_string,i))
    return len(index_appear.difference({-1}))

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)