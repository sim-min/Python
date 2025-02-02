Set = set()

s = input()
for i in range(len(s)):
    for j in range(i, len(s)):
        Set.add(s[i:j+1])

print(len(Set))