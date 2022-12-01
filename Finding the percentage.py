n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
check_name = input()
sum=0
for i in student_marks[check_name]:
    sum += i
p = sum/len(student_marks[check_name])
result = format(p,'.2f')
print(result)
