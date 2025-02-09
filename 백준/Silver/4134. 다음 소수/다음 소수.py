import sys
import math

N = int(sys.stdin.readline())

def prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if (x % i == 0):
            return False

    return True
    
for _ in range(N):
    num = int(sys.stdin.readline())
        
    if (num == 0) or (num == 1):
        print(2)
        continue
        
    while (True):
        if (prime(num)):
            print(num)
            break
            
        num +=1