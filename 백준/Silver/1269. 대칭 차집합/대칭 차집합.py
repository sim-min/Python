n, m = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

answer = len(A^B)
print(answer)