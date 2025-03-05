from collections import deque

N,K = map(int, input().split())
Circle = deque(range(1,N+1))

print(end='<')
while 1 < len(Circle):
  Circle.rotate(-K)
  print("%d" %Circle.pop(), end=', ')
print("%d" %Circle.pop(), end='>')