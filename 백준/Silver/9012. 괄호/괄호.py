t = int(input())
for i in range(t):
    stc = []
    test = list(input())
    for i in test:
        if i == '(':
            stc.append(i)
        else:
            if stc:
                stc.pop()
            else:
                print("NO")
                break
    else:
        if len(stc) == 0:
            print("YES")
        else:
            print("NO")