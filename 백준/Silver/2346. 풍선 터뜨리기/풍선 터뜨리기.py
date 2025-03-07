import sys
from collections import deque
input = sys.stdin.readline

balloon = int(input())
ballon_deq = deque(enumerate(map(int, input().split())))
answer = []

while ballon_deq:
    idx, paper = ballon_deq.popleft()
    answer.append(idx + 1)

    if paper > 0:
        ballon_deq.rotate(-(paper - 1))
    elif paper < 0:
        ballon_deq.rotate(-paper)

print(' '.join(map(str, answer)))