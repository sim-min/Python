n = int(input())
line = list(map(int, input().split()))
stack = []
number = 1
 
for i in line:
    stack.append(i)
 
    while stack and stack[-1] == number:
        stack.pop()
        number += 1
 
if stack:
    print('Sad')
else:
    print('Nice')