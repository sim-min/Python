n, m = map(int,input().split()) 
listen = []
see = []

for _ in range(n):
    listen.append(input())

for _ in range(m):
    see.append(input())

listen = set(listen)
see = set(see)

listen_see = set.intersection(listen,see)
print(len(listen_see))
listen_see = list(listen_see)
listen_see.sort()
for i in listen_see:
    print(i,end='\n')