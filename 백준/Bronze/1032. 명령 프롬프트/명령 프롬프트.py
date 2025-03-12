name = []
names = []
for i in range(int(input())):
    name.append(str(input()))

if len(name) == 1:
    print(name[0])
else:
    name_compare = name[0]
    for i in range(1, len(name)):
        for j in range(len(name[i])):
            if i == 1:
                if name_compare[j] == name[i][j]:
                    names.append(name_compare[j])
                else:
                    names.append('?')
            else:
                if names[j] != name[i][j]:
                    names[j] = '?'
print(''.join(names))