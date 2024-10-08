n = int(input())

f = 1
for i in range(1, n+1):
    print(" "*(n-i)+"*"*(f))
    f = f + 2