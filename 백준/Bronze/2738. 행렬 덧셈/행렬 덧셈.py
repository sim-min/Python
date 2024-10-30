n, m = map(int, input().split())
list1 = list()
list2 = list()

for i in range(n):
    list1.append(list(map(int, input().split())))
for i in range(n):
    list2.append(list(map(int, input().split())))

for i in range(n):
  for j in range(m):
    list1[i][j] += list2[i][j]
    
for i in range(n):
    print(*list1[i])