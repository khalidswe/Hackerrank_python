'''
n = int(input("number of student: "))
studentlist = []
for i in range(0,n+1):
    name = input()
    score =float(input())
    studentlist.append([name,score])

'''
list1 = []
score1 = []
for _ in range(int(input("enter student number: "))):
    name = input()
    score = float(input())
    list1.append([score,name])
    score1.append(score)
    lst = sorted(list1)
    scr = sorted(set(score1))
for i in list1:
    for j in i:
        if j == i[1] and score1[1] == i[0]:
            print(j)