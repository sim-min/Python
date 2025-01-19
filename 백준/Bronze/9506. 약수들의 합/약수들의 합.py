while True:
    n = int(input())
    if n == -1:
        break
    factor = []
    for i in range(1,n):
        if n % i == 0:
            factor.append(i)
    if sum(factor) == n:
        print(n, " = ", " + ".join(str(i) for i in factor), sep="")
    else:
        print(n, "is NOT perfect.")