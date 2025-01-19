n=int(input())
numbers=list(map(int, input().split()))
sorted_numbers=sorted(set(numbers))

d=dict()
for i in range(len(sorted_numbers)): 
    d[sorted_numbers[i]] = i

for i in  numbers:
    print(d[i], end=' ')