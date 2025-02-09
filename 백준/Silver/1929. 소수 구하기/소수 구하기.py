import math

n, m = map(int, input().split())
number = []

def prime(x):
    if x < 2 :
        return False
    for i in range(2, int(math.sqrt(x) + 1)):
    	if x % i == 0:
            return False
    return True

for i in range(n, (m + 1)) :
    if prime(i) == True :
        number.append(i)

for i in number :
    print (i)