from statistics import mean

n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    res = mean(scores)
    student_marks[name] = res

query_name = input()

print("%.2f "%student_marks[query_name])