dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = list(input())
time = 0

for i in word:
    for j in dial:
        if i in str(j):
            number = dial.index(j) + 3
            time += number
print(time)