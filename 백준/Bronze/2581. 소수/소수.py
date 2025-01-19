m=int(input())
n=int(input())

prime = []

for i in range(m, n+1):
    if i == 1:
        continue
    for j in range(2, i):
        if(i%j==0):
            break
    else:
        prime.append(i)
if sum(prime)==0:
    print(-1)
else:
    print(sum(prime))
    sorted(prime)
    print(prime[0])