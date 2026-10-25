#Nested Lists
#https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Find the second lowest grade
    grades = sorted(set([score for name, score in students]))
    second_lowest = grades[1]

    # Find all students with the second lowest grade
    second_lowest_students = [name for name, score in students if score == second_lowest]

    # Sort the names alphabetically and print them
    for name in sorted(second_lowest_students):
        print(name)
