N,M=map(int, input().split())
B=[0]*N
for x in range(M):
    i,j,k=map(int, input().split())
    for y in range(i, j+1):
        B[y-1]=k
for y in range(N):
    print(B[y], end=' ')