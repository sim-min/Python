num1, num2 = map(str, input().split())
num1 = int(num1, 2)
num2 = int(num2, 2)
number = num1+num2
print(bin(number)[2:])