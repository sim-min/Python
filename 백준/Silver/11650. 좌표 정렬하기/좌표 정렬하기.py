n = int(input())

dots = []

for i  in range(n):
    x, y = map(int, input().split())
    dots.append((x,y))
dots.sort()

for i in range(n):
    print(dots[i][0], dots[i][1])