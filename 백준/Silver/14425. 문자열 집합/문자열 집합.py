n, m = map(int,input().split())

lst = []
list =[]
for i in range(n) :
  a=input()
  lst.append(a)
for i in range(m) :
  b=input()
  list.append(b)
sum = 0

for i in list:
  if i in lst :
    sum += 1
print(sum)