number = list(input())
number.sort()

numbers = []
for i in range(len(number)):
    num = int(number[i])*(10**i)
    numbers.append(num)
print(sum(numbers))