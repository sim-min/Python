words = list(input().upper())
count = 0

for i in set(words):
    if count < words.count(i):
        count = words.count(i)
        result = i
    elif count == words.count(i):
        result = '?'

print(result)