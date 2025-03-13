color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

for i in range(3):
    co = str(input())
    if i==0:
        num1 = color.index(co)
    if i ==1:
        num2 = color.index(co)
    if i == 2:
        num3 = 10**color.index(co)

print(int(str(num1)+str(num2))*num3)