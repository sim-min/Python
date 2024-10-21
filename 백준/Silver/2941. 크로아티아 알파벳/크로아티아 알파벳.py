word = ['c=','c-','dz=','d-','lj','nj','s=','z=']
s = str(input())
for item in word:
    if item in s:
        s = s.replace(item,'1')
        
print(len(s))