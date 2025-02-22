n,m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(input()))

correct1 = ['B','W','B','W','B','W','B','W']
correct2 = ['W','B','W','B','W','B','W','B']

a = []
b = []

for _ in range(4):
    a.append(correct1)
    a.append(correct2)
    b.append(correct2)
    b.append(correct1)

count = 64
for i in range(n-7):
    for j in range(m-7):
        acnt=0
        bcnt=0
        for row in range(8):
            for col in range(8):
                if data[i+row][j+col] != a[row][col]:
                    acnt +=1

                if data[i+row][j+col] != b[row][col]:
                    bcnt +=1
        count = min(count, acnt, bcnt)
print(count)