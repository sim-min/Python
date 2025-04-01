num = list(map(int, input().split()))
number = 0
for i in num:
    number += i**2
print(number%10)