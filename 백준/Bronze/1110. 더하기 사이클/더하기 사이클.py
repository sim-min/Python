n = input().strip() 
if int(n) < 10:
    n = '0' + n 

new = n 
cnt = 0  

while True:
    number = int(new[0]) + int(new[1]) 
    new = new[1] + str(number % 10)  

    cnt += 1  
    if new == n:  
        break

print(cnt)
