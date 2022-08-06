def solution(s):
    answer = []
    list_s = s[2:-2].split('},{')
    list_s = [list(map(int,i.split(','))) for i in list_s]
    list_s.sort(key=len)
    
    for i in list_s:
        temp = list(set(i) - set(answer))
        answer.append(temp[0])
    
    return answer