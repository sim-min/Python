member = []
for _ in range(9):
    member.append(int(input()))

rest = sum(member) - 100
found = False

for i in range(9):
    for j in range(i + 1, 9):  
        if member[i] + member[j] == rest:
            result = [member[k] for k in range(9) if k != i and k != j]
            found = True
            break
    if found:
        break

for height in sorted(result):
    print(height)
