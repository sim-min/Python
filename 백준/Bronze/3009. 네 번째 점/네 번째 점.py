X = []
Y = []
for i in range(3):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

for j in X:
    if X.count(j) == 1:
        fin_x = j
    else:
        continue

for l in Y:
    if Y.count(l) == 1:
        fin_y = l
    else:
        continue
print(fin_x, fin_y)