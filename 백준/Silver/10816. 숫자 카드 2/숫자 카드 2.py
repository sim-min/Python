import sys
from collections import Counter

input = sys.stdin.readline

# 1. N 입력
N = int(input())

# 2. N개의 정수 입력받아 n에 저장
n = list(map(int, input().split()))

# 3. M 입력
M = int(input())

# 4. M개의 정수 입력받아 target에 저장
target = list(map(int, input().split()))

# 5. Counter 모듈로 개수 세기
count = Counter(n)

# 6. for문으로 알고 싶은 정수의 개수 출력
for i in range(M):
    if target[i] in count:
        print(count[target[i]], end=' ')
    else:
        print(0, end=' ')