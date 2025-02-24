import sys
note = []
for i in range(int(sys.stdin.readline())):
    money = int(sys.stdin.readline())
    if money == 0:
        note.pop()
    else:
        note.append(money)
print(sum(note))