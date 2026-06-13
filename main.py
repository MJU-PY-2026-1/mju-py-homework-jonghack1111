# 파일이름 :
# 작 성 자 :
#name = input('이름을 입력하세요 :')
#age = int(input('나이를 입력하세요 :'))

#distance = float(input('오늘 달린 거리 (km) :'))
#time = float(input('달린 시간 (분) :'))
#goal_distance = float(input('목표 거리(km) :'))
#pace = time / distance
all_users_data = []

def load_data():
    try:
        with open ('runners.txt', 'r', encoding = 'utf-8') as f:
            for line in f:
                data = line.strip().split(',')
                if len(data) >=6:
                    name = data[0]
                    age = int(data[1])
                    distance = float(data[2])
                    time = float(data[3])
                    goal_distance = float(data[4])
                    run_history = [float(x) for x in data[5:]]

                    all_users_data.append([name, age, distance, time, goal_distance, run_history])
        print('기존 러닝 데이터를 성공적으로 불러왔습니다.')
    except FileNotFoundError:
        print('저장된 파일이 없습니다 새로운 기록으로 시작합니다.')

def   save_data():
    with open('runners.txt', 'w', encoding = 'utf-8')as f:
        for user in all_users_data:
            history_str = ','.join(map(str, user[5]))
            f.write(f'{user[0]},{user[1]},{user[3]},{user[4]},{history_str}\n')
    print('전체 데이터가 안전하게 저장되었습니다.')

def input_data():
    try:
        name = input('이름을 입력하세요. :')
        age = int(input('나이를 입력하세요. :'))
        distance = float(input('오늘 달린 거리 (km) :'))
        time = float(input('달린 시간(분) :'))
        goal_distance = float(input('목표 거리(km) :'))


        print(f'최근 4번의 런닝 기록 입력')
        run_history = []
        for i in range(4):
            while True:
                try:
                    d = float(input(f'{i+1}번째 거리 : '))
                    if d<=0:
                        print('잘못된 값입니다 0보다 크게 입력하세요')
                        continue
                    run_history.append(d)
                    break
                except ValueError:
                    print('숫자로만 입력해주세요')
        all_users_data.append([name, age, distance, time, goal_distance, run_history])
        print('데이터가 이중 리스트에 성공적으로 추가되었습니다.')
    except ValueError:
        print('\n[오류]')





def view_data():
    print('\n-----[조회] 현재 입력된 데이터 목록-----')
    if not all_users_data:
        print('현재 입력된 데이터가 없습니다')
        return
    
    print(f'{'이름':<6}ㅣ{'나이':<4}ㅣ{'오늘거리':<6}ㅣ{'시간':<6}ㅣ{'목표거리':<6}ㅣ{'최근기록'}')
    for user in all_users_data:
        name = user[0]
        age = user[1]
        distance = user[2]
        time = user[3]
        goal = user[4]
        history = user[5]
        print(f'{name:<6}ㅣ{age:<4}ㅣ{distance:<8}ㅣ{time:<4}ㅣ{goal:<8}ㅣ{history}')


def analyze_data(distance, time, goal_distance, run_history):
    history = run_history.copy()
    pace = time/distance

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
    return pace, avg_distance, max_distance, today_index, goal_result, perfomance, grade, message, next_goal, recommanded_pace, history

def print_result():
    print('\n---[분석]전체 데이터 분석 결과---')
    if not all_users_data:
        print('분석할 데이터가 없습니다.')
        return
    for user in all_users_data:
        name, age, distance, time, goal_distance, originary_history = user
        res = analyze_data(distance, time, goal_distance, originary_history.copy())
    
        pace, avg_distance, max_distance, today_index, goal_result, perfomance, grade, message, next_goal, recommanded_pace, history = res
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

        print(f'\n유지된 최근 기록 : {history}')

load_data()

while True:
    print(f'===============================')
    print(f'1.데이터 입력')
    print('2.데이터 조회')
    print('3.전체 데이터 분석')
    print('4.저장 및 종료')
    print(f'===============================')
    menu = input('원하는 메뉴를 선택하세요 :')

    if menu == '1':
        input_data()
    elif menu == '2':
        view_data()
    elif menu == '3':
        print_result()
    elif menu == '4':
        print(f'프로그램을 종료합니다.')
        break
    else:
        print(f'잘못된 입력입니다. 다시 선택해주세요.')





