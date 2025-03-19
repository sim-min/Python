member = []
for i in range(int(input())):
    name = input()
    member.append(name[0])
player = []
for i in member:
    if member.count(i) > 4:
        player.append(i)
if player:
    for i in sorted(set(player)):
        print(i, end='')
else:
    print("PREDAJA")