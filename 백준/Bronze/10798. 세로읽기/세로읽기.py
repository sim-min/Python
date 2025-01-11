group = [input().split() for _ in range(5)]

result=''
for i in range(15):
    for j in range(5):
        try:
            result = result + group[j][0][i]
        except:
            pass

print(result)