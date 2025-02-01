triangle = list(map(int, input().split()))
max_l = max(triangle)
triangle.remove(max_l)
sum = sum(triangle)

if sum > max_l:
    print(sum + max_l)
else:
    print(sum + sum - 1)