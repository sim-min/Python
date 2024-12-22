numbers=[]
for i in range(10):
    num=int(input())
    rest=num%42
    numbers.append(rest)

fin = list(set(numbers))
print(len(fin))