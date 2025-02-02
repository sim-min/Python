import sys

A, B = map(int, sys.stdin.readline().split())

max = 1
i = 2
while (A >= i) and (B >= i):
    if (A % i == 0) and (B % i == 0):
        max *= i
        A //= i
        B //= i
    else:
        i += 1

print(max * A * B)