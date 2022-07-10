import math

def solution(progresses, speeds):
    answer = []
    cnt = 0
    day = 0
    
    for i in range(len(progresses)):
        if day*speeds[i] + progresses[i] >= 100:
            cnt += 1
            continue
        elif cnt > 0:
            answer.append(cnt)
            cnt = 0

        day += math.ceil((100 - progresses[i] - day*speeds[i])/speeds[i])
        cnt += 1
        
    answer.append(cnt)

    return answer