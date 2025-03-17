count = 0
for i in range(8):
    chess = list(input())
    for j in range(8):
        if i in [0, 2, 4, 6]:
            if j in [0, 2, 4, 6] and chess[j] == 'F':
                count = count+1
            else:
                count = count
        else:
             if j in [1, 3, 5, 7] and chess[j] == 'F':
                count = count+1 
             else:
                count = count
print(count)