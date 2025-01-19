n = int(input())
numbers = list(map(int, input().split()))
prime = 0

for i in numbers:
    if i == 1:
        continue
    for j in range(2, i):
        if(i%j==0):
            break
    else:
        prime+=1
print(prime)