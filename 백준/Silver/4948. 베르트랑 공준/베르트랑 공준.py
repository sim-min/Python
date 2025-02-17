import sys
input = sys.stdin.readline

def prime_numbers(n):
    arr = [i for i in range(n+1)]
    end = int(n ** (1/2))
    for i in range(2, end+1):
        if arr[i] == 0:
            continue
        for j in range(i*i, n+1, i):
            arr[j] = 0
    return [i for i in arr[2:] if arr[i]]

while 1:
    x = int(input().strip())
    if x == 0:
        break
    print(len(prime_numbers(2 * x)) - len(prime_numbers(x)))