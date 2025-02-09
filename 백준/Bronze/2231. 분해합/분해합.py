num = int(input())
creator = []

start = max(0, num - (9 * len(str(num))))
for i in range(start, num):  
    numbers = [int(digit) for digit in str(i)]

    if i + sum(numbers) == num:
        creator.append(i)
        break

if creator:
     print(creator[0])
else:
    print(0)