ans=0
answer=set()

for _ in range(int(input())):
    a=input()
    if a=='ENTER':
        answer.clear()
    else:
        if a in answer:
            pass
        else:
            answer.add(a)
            ans+=1
print(ans)