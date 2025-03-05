import sys
from collections import deque

input = sys.stdin.readline
d = deque()

for i in range(int(input())):
    order = input().strip().split()
    if order[0] == '1':
        d.appendleft(int(order[1]))
    elif order[0] == '2':
        d.append(int(order[1]))
    elif order[0] == '3':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
            d.popleft()
    elif order[0] == '4':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
            d.pop()
    elif order[0] == '5':
        print(len(d))
    elif order[0] == '6':
        print(int(not len(d)))
    elif order[0] == '7':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif order[0] == '8':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])