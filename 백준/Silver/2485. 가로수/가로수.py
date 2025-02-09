import sys
input = sys.stdin.readline
N = int(input())
trees = [int(input()) for _ in range(N)]

gaps = [trees[i+1] - trees[i] for i in range(0, len(trees)-1)]

def isGCD(num, gaps):
    for gap in gaps:
        if gap % num != 0:
            return False
    return True

import math
gcd = gaps[0]
for num in gaps:
    gcd = math.gcd(gcd, num)

result = int((trees[-1] - trees[0])/gcd - N + 1)
print(result)