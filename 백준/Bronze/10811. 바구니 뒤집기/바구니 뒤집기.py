n,m = map(int, input().split())

basket=[]
for a in range(1,n+1):
    basket.append(a)

for b in range(m):
    i,j=map(int, input().split())
    basket[i-1:j]=list(reversed(basket[i-1:j]))

print(*basket)