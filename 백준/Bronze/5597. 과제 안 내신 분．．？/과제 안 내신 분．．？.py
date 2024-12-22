students = []

for i in range(1,31):
    students.append(i)

submit=0
for j in range(28):
    submit= int(input())
    students.remove(submit)

print(students[0])
print(students[1])