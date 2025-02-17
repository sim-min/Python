number = int(input())
real = list(map(int, input().split()))
real.sort()
print(int(real[0]*real[-1]))