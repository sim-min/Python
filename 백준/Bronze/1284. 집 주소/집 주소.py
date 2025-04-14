while True:
    n = input()
    if n=='0':
        break
    else:
        cm = 1
        for i in n:
            if i=='1':
                cm = cm+3
            elif i=='0':
                cm = cm+5
            else:
                cm = cm+4
        print(cm)