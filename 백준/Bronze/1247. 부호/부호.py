for _ in range(3):
    plus = 0
    for _ in range(int(input())):
        num = int(input())
        plus += num
        
    if plus == 0:
        print(0)
    elif plus < 0:
        print("-")
    else:
        print("+")