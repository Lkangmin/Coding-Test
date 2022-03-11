def solution(dartResult):
    bonus = {'S':1, 'D':2, 'T':3}
    total = []
    digit = '' # 10이 존재하기 때문에 숫자를 쌓아가는 방식
    cnt = -1  # 해당 점수가 몇번째 점수인지 확인
    
    for i in dartResult:
        # 숫자일 경우
        if i.isdigit():
            digit += i
        # 보너스일 경우
        elif i in bonus.keys():
            total.append(int(digit)**bonus[i])
            digit = ''
            cnt += 1
        # 스타상일 경우
        elif i == '*':
            total[cnt] *= 2
            if cnt > 0:
                total[cnt-1] *= 2
        # 아차상일 경우
        elif i == '#':
            total[cnt] *= -1

    return sum(total)