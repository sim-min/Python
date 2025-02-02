import math
a, b = map(int, input().split())
c, d = map(int, input().split())

e = a*d+c*b
f = b*d

max = math.gcd(e,f)

print(int(e/max), int(f/max))