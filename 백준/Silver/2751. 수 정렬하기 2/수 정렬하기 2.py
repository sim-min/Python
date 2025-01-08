import sys
n = int(sys.stdin.readline())
numbers = []

for i in range(n):
    num = int(sys.stdin.readline())
    numbers.append(num)
numbers.sort()

for j in range(n):
    print(numbers[j])