import sys
input = sys.stdin.readline
n = int(input())
card = set(map(int,input().split()))
m = int(input())
numbers = list(map(int,input().split()))

for i in range(m):
    if numbers[i] not in card:
        print(0, end=' ')
    else:
        print(1, end=' ')