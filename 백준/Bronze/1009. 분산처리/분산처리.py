for i in range(int(input())):
    a, b = map(int, input().split())
    number = pow(a,b,10)
    if number != 0:
        print(number)
    else:
        print(10)