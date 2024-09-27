A,B,C=map(int,input().split())
if B>=C: #판매가가 가변가보다 적으면 손익분기점은 존재할 수 없음. 
    print(-1)
else:
    print((A//(C-B))+1)