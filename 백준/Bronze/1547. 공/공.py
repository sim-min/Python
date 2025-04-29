cup = [1, 2, 3]
m = int(input())
for i in range(m):
    x, y =map(int, input().split())
    cup[x-1], cup[y-1] = cup[y-1], cup[x-1]
print(cup.index(1)+1)