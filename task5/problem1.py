#Find the Runner-Up Score!
#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())

    arr = map(int, input().split())

    list_arr=[]

    list_arr.extend(arr)

    unique_set=set(list_arr)

    new_list=sorted(unique_set,reverse=True)

    second_score=new_list[1]

    print(second_score)