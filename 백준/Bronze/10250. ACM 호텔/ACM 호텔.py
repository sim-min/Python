t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    roomn = n//h #룸 넘버는 몫에 따라 결정됨. 오른쪽으로 갈 수록 호수의 크기가 +1 -> 몫과 같다. 
    roomh = n%h
    if roomh == 0: #손님의 순서가 h로 딱 떨어짐 -> 최고층 배정.
        roomh = h
    else: #딱 떨어지지 않을 경우 -> 몫에 +1을 해주어야 함, 1.xx는 2로 계산.
        roomn +=1
    
    if roomn < 10: #101호가 11호로 출력되는 것 방지
        print(str(roomh)+"0"+str(roomn))
    else:
        print(str(roomh)+str(roomn))