fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]

for i in range(18, 21):
    fibonacci.append(fibonacci[i-1]+fibonacci[i-2])

n = int(input())
print(fibonacci[n])