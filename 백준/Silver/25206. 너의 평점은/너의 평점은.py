rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

score = 0  # score 변수 초기화
time = 0  # time 변수 초기화

for i in range(20):
    name, time_str, level = input().split()
    time_val = float(time_str)  # 입력받은 시간 문자열을 숫자로 변환
    
    if level != 'P':
        score += time_val * (grade[rating.index(level)])
        time += time_val  # time 변수에 누적 시간 추가
    else:
        continue

print(score / time)