import math
N = list((input())) 
first = []
last = []

for i in range(1, len(N)):
    left = N[:i]
    right = N[i:]

    left_prod = math.prod([int(x) for x in left])
    right_prod = math.prod([int(x) for x in right])

    first.append(left_prod)
    last.append(right_prod)

result = []
for j in range(len(first)):
    if first[j] == last[j]:
        result.append("YES")
    else:
        result.append("NO")

if "YES" in result:
    print("YES")
else:
    print("NO")