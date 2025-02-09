import sys
input = sys.stdin.readline

numbers = [0]*10001 #정수의 크기가 10,000 이하로 한정 -> 10,001의 빈 깡통 생성.
for k in range(int(input())):
    num = int(input()) #숫자 입력받기
    numbers[num] += 1 #입력 받은 숫자 인덱스의 깡통으로 이동하여 숫자 올리기기

for i in range(10001):
   if numbers[i] != 0:
       for j in range(numbers[i]):
            print(i)