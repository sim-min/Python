n=int(input())
title = []
for i in range(666, 8000000):
    if '666' in str(i):
        title.append(i)
print(title[n-1])