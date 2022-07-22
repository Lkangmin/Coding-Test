def solution(s):
    answer = 1
    
    a = []
    
    for i in s:
        if a and a[-1] == i:
            del a[-1]
        else:
            a.append(i)
    
    if a:
        answer = 0
    
    return answer