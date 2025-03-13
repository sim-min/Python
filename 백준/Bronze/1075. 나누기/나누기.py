n=input()
f=int(input())
answer = n[:-2]

for i in range(100):  
    i_str = f"{i:02d}" 
    n2 = int(answer + i_str)
    if n2 % f == 0:
        print(i_str)
        break