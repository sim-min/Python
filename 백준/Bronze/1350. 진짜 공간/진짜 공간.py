N = int(input())
file = list(map(int, input().split()))
clu = int(input())
space = N
for i in file:
    if i > clu:
        space += (i-1)//clu
    elif i == 0:
        space -= 1
print(clu*space)