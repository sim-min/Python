X, Y = input().split()
revX = int(X[::-1])
revY = int(Y[::-1])
result = revX + revY
print(int(str(result)[::-1]))