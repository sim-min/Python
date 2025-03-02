import sys

while True:
    n = sys.stdin.readline().rstrip()
    A = []

    if n == ".": #종료 조건
        break

    for i in n: # 입력값을 하나하나 추가
        if i == '(' or i == '[': # 여는 괄호면 A에 추가
            A.append(i)  

        elif i == ')' :
            if len(A) != 0 and A[-1] == "(": # 길이가 0이 아니고 마지막 요소가'('일때 i가 ')'면 요소 삭제
                A.pop()  # 요소 삭제
            else:
                A.append(i)  # 세트 안맞으면 A에 추가
              
        elif i == ']' :           
            if len(A) != 0 and A[-1] == "[":
                    A.pop() 
            else:
                A.append(i)
                
    if len(A) == 0:
        print("yes")
    else:
        print("no") 