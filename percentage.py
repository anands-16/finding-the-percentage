#finding percentage of subject 
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
li = student_marks[query_name]
j = 0
for _ in li:
    j = j + _
k = j/3
print("%.2f"%k)
