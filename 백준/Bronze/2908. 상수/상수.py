A, B = map(int, input().split())

R_A = int(str(A)[::-1])
R_B = int(str(B)[::-1])

if R_A > R_B:
    print(R_A)
else:
    print(R_B)