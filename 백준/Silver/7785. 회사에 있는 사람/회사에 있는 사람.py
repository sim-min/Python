number = int(input())
member = dict()

for i in range(number):
    name, status = input().split()
    member[name]= status

enter_member = []
for key, value in member.items():
    if value == "enter":
        enter_member.append(key)

enter_member.sort(reverse=True)

for i in enter_member:
    print(i)