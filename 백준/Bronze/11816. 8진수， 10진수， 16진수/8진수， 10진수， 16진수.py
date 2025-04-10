X = input()
if X[0:2] == '0x':
    print(int(X[2:], 16))
elif X[0] == '0':
    print(int(X, 8))
else:
    print(int(X))