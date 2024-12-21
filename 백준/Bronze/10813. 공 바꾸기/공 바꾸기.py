n,m=map(int, input().split())
basket=[]
for a in range(n):
    basket.append(a+1)

for b in range(m):
    i,j=map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

for c in basket:
    print(c, end=' ')