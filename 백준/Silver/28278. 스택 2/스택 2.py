import sys
st = []

for _ in range(int(sys.stdin.readline())):
    a = sys.stdin.readline().split()
    
    if a[0] == '1':
        st.append(a[1])

    elif a[0] == '2':
        if st:
            print(st.pop())
        else:
            print(-1)

    elif a[0] == '3':
        print(len(st))

    elif a[0] == '4':
        if st:
            print(0)
        else:
            print(1)

    elif a[0] == '5':
        if st:
            print(st[-1])
        else:
            print(-1)