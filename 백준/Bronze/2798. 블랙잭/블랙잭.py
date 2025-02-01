n, m = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()
result=[]

for i in range(len(cards)-2):
    for j in range(i+1,len(cards)-1):
        for k in range(j+1,len(cards)):
            if cards[i]+cards[j]+cards[k]>m:
                continue
            else:
                result.append(cards[i]+cards[j]+cards[k])
                
print(max(result))