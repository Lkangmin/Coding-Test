from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    total = len(dungeons)
    
    for i in permutations(range(total), total):
        temp = k
        cnt = 0
        for j in i:
            if temp >= dungeons[j][0]:
                temp -= dungeons[j][1]
                cnt += 1
            else:
                break
        answer = max(answer, cnt)
    
    return answer