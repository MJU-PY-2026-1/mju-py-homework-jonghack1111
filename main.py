# 파일이름 :
# 작 성 자 :
name = input('이름을 입력하세요 :')
age = int(input('나이를 입력하세요 :'))

distance = float(input('오늘 달린 거리 (km) :'))
time = float(input('달린 시간 (분) :'))
goal_distance = float(input('목표 거리(km) :'))

pace = time / distance

run_history = []
print(f'최근 4번의 런닝 기록 입력')

for i in range(4):
    d = float(input(f'{i+1}번째 거리 :'))
    if d <=0:
        print(f'잘못된 값입니다. 다시 입력하세요.')
        continue
    run_history.append(d)

run_history.append(distance)
run_history.sort()

if len(run_history) > 4:
    run_history.remove(run_history[0])

avg_distance = sum(run_history) / len(run_history)
max_distance = max(run_history)
today_index = run_history.index(distance)

if distance > avg_distance and pace < 7:
    goal_result = '달성성공!!!'
else:
    goal_result = '달성실패'

if distance > avg_distance and pace < 7:
    perfomance = '최근 평균보다 뛰어납니다!!!'
else:
    perfomance = '조금 더 노력해봅시다'

if pace <=5 and distance >= avg_distance:
    grade = 'A'
elif pace <= 6:
    grade = 'B'
elif pace <= 7:
    grade = 'C'
else:
    grade = 'D'

if grade == 'A':
    if goal_result == '달성성공!!!':
        message = '완벽한 러닝입니다!'
    else:
        message = '실력은 충분합니다.'
elif grade == 'B':
    message = '조금만 더 하면 A!'
elif grade == 'C':
    message = '꾸준히 하면 늘어요~'
else:
    message = '내일은 더 잘해봅시다..'

next_goal = goal_distance

if goal_result == '달성성공!!!' and distance > avg_distance:
    next_goal += 1
else:
    next_goal -= 0.5

if pace > 5 :
    recommanded_pace = pace - 0.2
else:
    recommanded_pace = pace

print(f'\n=====러닝결과=====')
print(f'이름 : {name}, 나이 : {age}')
print(f'오늘 거리 : {distance}km / 시간 : {time}분')
print(f'페이스 : {pace}분/km')
print(f'목표 달성 여부 : {goal_result}')
print(f'평균 거리 : {avg_distance}km')
print(f'성과 평가 : {perfomance}')
print(f'러닝 등급 : {grade}')
print(f'동기부여 : {message}')
print(f'최고 기록 : {max_distance}')
print(f'오늘 기록 순위 : {today_index}')

print(f'\n=====내일 목표=====')
print(f'추천 거리 : {next_goal}km')
print(f'추천 페이스 : {recommanded_pace}분/km')

print(f'\n유지된 최근 기록 : {run_history}')




