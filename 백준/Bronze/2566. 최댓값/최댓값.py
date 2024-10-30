whole = []
part = [] 
num=0
N=0
M=0

for i in range(9):
    part = list(map(int,input().split()))
    whole.append(part)

for i in range(9):
  for j in range(9):
    if num < whole[i][j]:
        num = whole[i][j]
        N=i
        M=j

print(num)
print(N+1,M+1)