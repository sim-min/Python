n=int(input())
five = []
three = []
for i in range(1, 1001):
    five.append(5*i)
for j in range(1, 1667):
    three.append(3*j)
bag=[]
for k in range(len(three)):
    for l in range(len(five)):
        if three[k]+five[l] == n:
            bag.append(k+l+2)
        elif n == three[k]:
            bag.append(k+1)
        elif n== five[l]:
            bag.append(l+1)
        else:
            continue
if not bag:
    print(-1)
else:
    print(min(bag))  